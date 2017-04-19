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

public class RunDiffusion {


	public static User findUser(ArrayList<User> users, String username)
	{
		for (int i = 0; i < users.size(); i++)
		{
			if (users.get(i).ID.equals(username))
			{
				return users.get(i);
			}
		}
		return null;
	}

	public static User findUserFriendNum(ArrayList<User> users, String friendNum)
	{
		for (int i = 0; i < users.size(); i++)
		{
			if (users.get(i).friendNumber.equals(friendNum))
			{
				return users.get(i);
			}
		}
		return null;
	}

	public static void addPosts(String csvPosts, ArrayList<User> users) throws IOException, ParseException
	{
		BufferedReader CSVItem2 = new BufferedReader(new FileReader(csvPosts));

		CSVItem2.readLine();
		String data2 = CSVItem2.readLine();
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"); 
		while (data2 != null){
			String[] dataArray2 = data2.split(",");
			{
				Post thispost = new Post();
				String title = dataArray2[1];
				if (dataArray2.length > 4)
				{
					for (int loop = 0; loop < dataArray2.length-4; loop++)
					{
						title = title+","+dataArray2[loop+2];
					}
				}
				String date = dataArray2[dataArray2.length-1];
				date = date.substring(1, date.length()-1);
				thispost.createPost(dataArray2[0], title, df.parse(date));
				findUser(users, dataArray2[0]).addPost(thispost);
			}
			data2 = CSVItem2.readLine(); // Read next line of data.
		}
		CSVItem2.close();
	}

	public static void addFriends(String csvPosts, ArrayList<User> users) throws IOException, ParseException
	{
		BufferedReader CSV = new BufferedReader(new FileReader(csvPosts));

		CSV.readLine();
		String data = CSV.readLine();
		while (data != null){
			String[] dataArray = data.split(",");
			{
				if (dataArray[1].equals("0"))
				{
					User u1 = findUserFriendNum(users, dataArray[2]);
					User friend1 = findUser(users, dataArray[0]);
					if (u1 != null && friend1 != null)
					{
						u1.addFriend(friend1);
					}
				}
			}
			data = CSV.readLine(); // Read next line of data.
		}
		CSV.close();
	}

	public static void createUsers(String csvPosts, ArrayList<User> users) throws IOException, ParseException
	{
		BufferedReader CSV = new BufferedReader(new FileReader(csvPosts));

		CSV.readLine();
		String data = CSV.readLine();
		while (data != null){
			String[] dataArray = data.split(",");
			{
				if (dataArray[1].equals("1"))
				{
					User thisUser = new User();
					thisUser.createUser(dataArray[0], dataArray[2], new ArrayList<User>(), new ArrayList<Post>());
					users.add(thisUser);
				}
			}
			data = CSV.readLine(); // Read next line of data.
		}
		CSV.close();
	}

	public static void buildNodes(ArrayList<User> users, ArrayList<Node> nodes, ArrayList<Node2> nodes2)
	{
		for (int i = 0; i < users.size(); i++)
		{
			User user = users.get(i);
			for (int j = 0; j < user.friendList.size(); j++)
			{
				User friend = user.friendList.get(j);
				int weight = 0;
				for (int k = 0; k < user.postList.size(); k++)
				{
					Post userPost = user.postList.get(k);
					for (int l = 0; l < friend.postList.size(); l++)
					{
						Post friendPost = friend.postList.get(l);
						if (friendPost.title.equals(userPost.title) && friendPost.created.before(userPost.created))
						{
							Node thisNode = new Node();
							thisNode.createNode(user.ID, friend.ID, userPost.title, userPost.created, friendPost.created);
							nodes.add(thisNode);
							weight++;
						}
					}
				}
				if (weight > 0)
				{
					Node2 node2 = new Node2();
					node2.createNode(user.ID, friend.ID, weight);
					nodes2.add(node2);
				}
			}
		}
	}
	
	public static void printNodes2ToCSV(ArrayList<Node2> nodes2) throws FileNotFoundException
	{
		PrintWriter pw = new PrintWriter(new File("network.csv"));
		pw.write("userId"+','+"friendId"+','+"weight"+'\n');
		for (int i = 0; i < nodes2.size(); i++)
		{
			pw.write(nodes2.get(i).ID+','+nodes2.get(i).friendId+','+nodes2.get(i).weight+'\n');
		}
		pw.close();
	}
	
	public static void printNodesToCSV(ArrayList<Node> nodes) throws FileNotFoundException
	{
		PrintWriter pw = new PrintWriter(new File("data.csv"));
		pw.write("userId"+','+"friendId"+','+"title"+','+"created"+','+"friendCreated"+'\n');
		for (int i = 0; i < nodes.size(); i++)
		{
			pw.write(nodes.get(i).ID+','+nodes.get(i).friendId+','+nodes.get(i).title+','+nodes.get(i).created+','+nodes.get(i).friendCreated+'\n');
		}
		pw.close();
	}


	public static void main(String[] args) throws IOException, ParseException {

		ArrayList<User> users = new ArrayList<User>();
		ArrayList<Node> nodes = new ArrayList<Node>();
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();
		createUsers("contacts.csv", users);
		addFriends("contacts.csv", users);
		addPosts("items.csv", users);
		buildNodes(users, nodes, nodes2);
		printNodesToCSV(nodes);
		printNodes2ToCSV(nodes2);
	}
}
