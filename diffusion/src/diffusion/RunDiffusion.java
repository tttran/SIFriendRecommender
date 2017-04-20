package diffusion;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

/**
 * @author Sarah Devlin
 * 
 * This is the main class that runs the diffusion algorithm
 *
 */
public class RunDiffusion {
	
	/**
	 * This main method will run the code.  Make sure to modify the csv names in this method if you decide to use different data.
	 * 
	 * @param args
	 * @throws IOException
	 * @throws ParseException
	 */
	public static void main(String[] args) throws IOException, ParseException {

		ArrayList<User> users = new ArrayList<User>();  // A list to hold all user instances deemed relevant to diffusion
		ArrayList<Node> nodes = new ArrayList<Node>();  // A list of nodes that hold each instance of diffusion
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();  // A list of different nodes that hold each relationship experiencing diffusion
		/**
		 *   The "contacts.csv" was derived using the following query:
		 *   select nick, self, uid from friendica_e1r2.contact where nick not like "admin" and nick in (Select distinct `author-name` as id from friendica_e1r2.item where wall = 1  and (file = "<news>" or file = "<TES>")) limit 0,2000;
		 */
		createUsers("contacts.csv", users);  // creates the list of users from the CSV
		addFriends("contacts.csv", users);  // connects the list of friends to each user using the CSV
		/**
		 *   The "items.csv" was derived using the following query:
		 *   select `author-name` as id, title, created from friendica_e1r2.item where (file = "<news>" or file = "<TES>") and wall=1 group by `author-name`, title, file order by id;
		 */
		addPosts("items.csv", users);   // adds the list of posts to each user using the CSV
		buildNodes(users, nodes, nodes2);  // builds the two different networks of nodes
		printNodesToCSV(nodes);  // prints each instance of diffusion (stored in Node class type) to a CSV
		printNodes2ToCSV(nodes2);  // prints each diffusion relationship (stored in Node2 class type) to a CSV
		printLatticeToCSV(nodes2);  // prints lattice node2s to a CSV (called lattice_network.csv)
		printSmallWorldToCSV(nodes2); // prints smallworld node2s to a CSV (called smallWorld_network.csv)
		
	}

	/**
	 * A helper method that returns the user instance who matches the username provided.
	 * 
	 * @param users		the arraylist storing all users
	 * @param username	the username to find
	 * @return 			the user instance whose username matches the username passed in, else return null
	 */
	public static User findUser(ArrayList<User> users, String username) {
		for (int i = 0; i < users.size(); i++) {
			if (users.get(i).ID.equals(username)) {
				return users.get(i);
			}
		}
		return null;
	}

	/**
	 * A helper method that returns the user instance with the "friendNum" (which is a key that matches friendships) provided
	 * 
	 * @param users			The list of all users
	 * @param friendNum		The number corresponding to one users list of relationships.  It helps identify friends within the database (store contacts.csv)
	 * @return				the user instance whose friendnum matches the friendnum passed in, else return null
	 */
	public static User findUserFriendNum(ArrayList<User> users, String friendNum) {
		for (int i = 0; i < users.size(); i++) {
			if (users.get(i).friendNumber.equals(friendNum)) {
				return users.get(i);
			}
		}
		return null;
	}
	
	/**
	 * Given an empty arrayList of users, it will populate the list with users by reading the CSV
	 * 
	 * @param csvUsers 				the name of the CSV holding user data
	 * @param users					the empty arrayList of users
	 * @throws IOException
	 * @throws ParseException
	 */
	public static void createUsers(String csvUsers, ArrayList<User> users) throws IOException, ParseException {
		BufferedReader CSV = new BufferedReader(new FileReader(csvUsers)); 
		CSV.readLine(); // skips the first line because it holds CSV column titles
		String data = CSV.readLine(); // reads the next line and stores it as "data"
		while (data != null) {
			String[] dataArray = data.split(","); // splits the data into columns
			{
				if (dataArray[1].equals("1")) { 	// The value here indicates 0 for friend, 1 for user
					User thisUser = new User(dataArray[0], dataArray[2], new ArrayList<User>(), new ArrayList<Post>()); // create user instance
					users.add(thisUser); // add the user to the list
				}
			}
			data = CSV.readLine(); // Read next line of data.
		}
		CSV.close(); // close the CSV
	}

	/**
	 * Given a populated arrayList of users, it will populate the friendlist of each user by reading the CSV
	 * 
	 * @param csvFriends		The name of the CSV holding friend data
	 * @param users				The populated arrayList of users
	 * @throws IOException
	 * @throws ParseException
	 */
	public static void addFriends(String csvFriends, ArrayList<User> users) throws IOException, ParseException {
		BufferedReader CSV = new BufferedReader(new FileReader(csvFriends));
		CSV.readLine();		// skips the first line because it holds CSV column titles
		String data = CSV.readLine();	// reads the next line and stores it as "data
		while (data != null) {
			String[] dataArray = data.split(","); // splits the data into columns
			{
				if (dataArray[1].equals("0")) {  // The value here indicates 0 for friend, 1 for user
					User u1 = findUserFriendNum(users, dataArray[2]);  // use the find friend method to find the user whose friend this is
					User friend1 = findUser(users, dataArray[0]);		// find the instance of the friend in the user arrayList
					if (u1 != null && friend1 != null) {				// if both the friend and the user were found
						u1.addFriend(friend1);							// add the friend to the users friend arrayList
					}
				}
			}
			data = CSV.readLine(); // Read next line of data.
		}
		CSV.close();  // close the CSV
	}

	/**
	 * Given a populated arrayList of users, it will populate the postList of each user by reading the CSV
	 * 
	 * @param csvPosts			The name of the CSV holding post data
	 * @param users				The populated arayList of users
	 * @throws IOException
	 * @throws ParseException
	 */
	public static void addPosts(String csvPosts, ArrayList<User> users) throws IOException, ParseException {
		BufferedReader CSV = new BufferedReader(new FileReader(csvPosts));
		CSV.readLine(); //skips the first line because it holds CSV column titles
		String data = CSV.readLine(); // reads the next line and stores it as "data"
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");  // creates a date format to apply to date strings
		while (data != null) { 
			String[] dataArray2 = data.split(",");  //splits the data into columns
			{
				String title = dataArray2[1]; // the "title" column may contain commas
				if (dataArray2.length > 4) {  
					for (int loop = 0; loop < dataArray2.length - 4; loop++) {
						title = title + "," + dataArray2[loop + 2];  //  adds any delimited chunks of the title back into the title
					}
				}
				String date = dataArray2[dataArray2.length - 1];  // stores the date as a string
				date = date.substring(1, date.length() - 1);  // removes any quotations from the date string
				Post thispost = new Post(dataArray2[0], title, df.parse(date));  //parses the string into a date and creates a post object
				findUser(users, dataArray2[0]).addPost(thispost);  // finds the user who created the post and adds it to their post list
			}
			data = CSV.readLine(); // Read next line of data.
		}
		CSV.close(); // close the CSV
	}

	/**
	 * This method creates both arrayLists of node types (processing the data) so that it is in a more usable format
	 * 
	 * @param users			The populated arrayList of user that has friends and posts added to their lists
	 * @param nodes			The empty arrayList of nodes which will track each instance of diffusion
	 * @param nodes2		The empty arrayList of nodes2 which will track every relationship of diffusion
	 */
	public static void buildNodes(ArrayList<User> users, ArrayList<Node> nodes, ArrayList<Node2> nodes2) {
		for (int i = 0; i < users.size(); i++) {  // iterate through all users
			User user = users.get(i);
			for (int j = 0; j < user.friendList.size(); j++) {  // iterate through each friend in each user's friendList
				User friend = user.friendList.get(j);
				int weight = 0;		// tracks the number of titles this friend took before this user
				for (int k = 0; k < user.postList.size(); k++) {  // iterate through each post for each user
					Post userPost = user.postList.get(k);
					for (int l = 0; l < friend.postList.size(); l++) {  // iterate through each post for each friend
						Post friendPost = friend.postList.get(l);
						if (friendPost.title.equals(userPost.title) && friendPost.created.before(userPost.created)) {  	// if the friend's post's title matches the user's 
																														//post's title and the friend's post was created first
							Node thisNode = new Node(user.ID, friend.ID, userPost.title, userPost.created,				// create a node, this user has diffusion from this friend
									friendPost.created);
							nodes.add(thisNode);	// add the node to the arrayList
							weight++;				// increase the weight of this diffusion relationship
						}
					}
				}
				if (weight > 0) {  // if this user and this friend had any posts showing diffusion
					Node2 node2 = new Node2(user.ID, friend.ID, weight);  // create a node2 (diffusion relationship node)
					nodes2.add(node2); // add the node to the arrayList
				}
			}
		}
	}
	
	/**
	 * This method prints nodes to a CSV
	 * 
	 * @param nodes			The arrayList of nodes showing each instance of diffusion
	 * @throws FileNotFoundException
	 */
	public static void printNodesToCSV(ArrayList<Node> nodes) throws FileNotFoundException {
		PrintWriter pw = new PrintWriter(new File("data.csv"));  // You can change the name of the output CSV here
		pw.write("userId" + ',' + "friendId" + ',' + "title" + ',' + "created" + ',' + "friendCreated" + '\n');  // write the column headers
		for (int i = 0; i < nodes.size(); i++) { // iterate through each node
			pw.write(nodes.get(i).ID + ',' + nodes.get(i).friendId + ',' + nodes.get(i).title + ','
					+ nodes.get(i).created + ',' + nodes.get(i).friendCreated + '\n');  // write the node to the CSV
		}
		pw.close(); // close the file
	}

	/**
	 * This method prints nodes2 to a CSV
	 * 
	 * @param nodes2		The arrayList of nodes2 showing each relationship with diffusion
	 * @throws FileNotFoundException
	 */
	public static void printNodes2ToCSV(ArrayList<Node2> nodes2) throws FileNotFoundException {
		PrintWriter pw = new PrintWriter(new File("network.csv"));  // you can change the name of the output CSV here
		pw.write("userId" + ',' + "friendId" + ',' + "weight" + '\n');  // write the column headers
		for (int i = 0; i < nodes2.size(); i++) {  // iterate through each node
			pw.write(nodes2.get(i).ID + ',' + nodes2.get(i).friendId + ',' + nodes2.get(i).weight + '\n');  // write the node to the CSV
		}
		pw.close(); // close the file
	}
	
	/**
	 * This method prints only Lattice nodes2 to a CSV
	 * 
	 * @param nodes2		The arrayList of nodes2 showing each relationship with diffusion
	 * @throws FileNotFoundException
	 */
	public static void printLatticeToCSV(ArrayList<Node2> nodes2) throws FileNotFoundException {
		PrintWriter pw = new PrintWriter(new File("lattice_network.csv"));  // you can change the name of the output CSV here
		pw.write("userId" + ',' + "friendId" + ',' + "weight" + '\n');  // write the column headers
		for (int i = 0; i < nodes2.size(); i++) {  // iterate through each node
			int id = Integer.parseInt(nodes2.get(i).ID.substring(1, nodes2.get(i).ID.length()));  // get number only (no u in id) and convert to int
			if (id >= 4001 && id <= 4128)  //  If id in this range, its in lattice
			{
			pw.write(nodes2.get(i).ID + ',' + nodes2.get(i).friendId + ',' + nodes2.get(i).weight + '\n');  // write the node to the CSV
			}
		}
		pw.close(); // close the file
	}
	
	/**
	 * This method prints only SmallWorld nodes2 to a CSV
	 * 
	 * @param nodes2		The arrayList of nodes2 showing each relationship with diffusion
	 * @throws FileNotFoundException
	 */
	public static void printSmallWorldToCSV(ArrayList<Node2> nodes2) throws FileNotFoundException {
		PrintWriter pw = new PrintWriter(new File("smallWorld_network.csv"));  // you can change the name of the output CSV here
		pw.write("userId" + ',' + "friendId" + ',' + "weight" + '\n');  // write the column headers
		for (int i = 0; i < nodes2.size(); i++) {  // iterate through each node
			int id = Integer.parseInt(nodes2.get(i).ID.substring(1, nodes2.get(i).ID.length())); // get number only (no u in id) and convert to int
			if (id >= 4129 && id <= 4256)  //  If id in this range, its in smallWorld
			{
			pw.write(nodes2.get(i).ID + ',' + nodes2.get(i).friendId + ',' + nodes2.get(i).weight + '\n');  // write the node to the CSV
			}
		}
		pw.close(); // close the file
	}
}
