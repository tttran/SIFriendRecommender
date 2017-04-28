package diffusion;
import java.io.File;
import java.io.IOException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Scanner;
import junit.framework.TestCase;

/**
 * @author Matthew Blumen
 * 
 * This is the test class that tests the diffusion algorithm
 *
 */
public class RunDiffusionTest extends TestCase {
	/**
	 * This method will set up all necessary fields
	 */
	public void setUp() {
		// There is no need for code here
	}
	
	/**
	 * This method will test the findUser() function.
	 * This is a unit test that tests individual method functionality.
	 */
	public void testFindUser() {
		ArrayList<User> users = new ArrayList<User>();
		for (int i = 0; i < 10; i++) {
			users.add(new User("" + i, "" + i + i, null, null));
		}
		
		User test0 = RunDiffusion.findUser(users, "0");
		assertTrue(test0.ID.equals("0"));
		assertTrue(test0.friendNumber.equals("00"));
		
		User test1 = RunDiffusion.findUser(users, "1");
		assertTrue(test1.ID.equals("1"));
		assertTrue(test1.friendNumber.equals("11"));
		
		User test8 = RunDiffusion.findUser(users, "8");
		assertTrue(test8.ID.equals("8"));
		assertTrue(test8.friendNumber.equals("88"));
		
		User test9 = RunDiffusion.findUser(users, "9");
		assertTrue(test9.ID.equals("9"));
		assertTrue(test9.friendNumber.equals("99"));
	}
	
	/**
	 * This method will test the findFriendNum() function.
	 * This is a unit test that tests individual method functionality.
	 */
	public void testFindUserFriendNum() {
		ArrayList<User> users = new ArrayList<User>();
		for (int i = 0; i < 10; i++) {
			users.add(new User("" + i, "" + i + i, null, null));
		}
		
		User test0 = RunDiffusion.findUserFriendNum(users, "00");
		assertTrue(test0.ID.equals("0"));
		assertTrue(test0.friendNumber.equals("00"));
		
		User test1 = RunDiffusion.findUserFriendNum(users, "11");
		assertTrue(test1.ID.equals("1"));
		assertTrue(test1.friendNumber.equals("11"));
		
		User test8 = RunDiffusion.findUserFriendNum(users, "88");
		assertTrue(test8.ID.equals("8"));
		assertTrue(test8.friendNumber.equals("88"));
		
		User test9 = RunDiffusion.findUserFriendNum(users, "99");
		assertTrue(test9.ID.equals("9"));
		assertTrue(test9.friendNumber.equals("99"));
		
	}
	
	/**
	 * This method will test the createUsers() function.
	 * This is a unit test that tests individual method functionality.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testCreateUsers() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		RunDiffusion.createUsers("contacts.csv", users);
		assertEquals(users.size(), 157);
		
		User front = users.get(0);
		assertFalse(front.ID.equals(""));
		assertFalse(front.friendNumber.equals(""));
		
		User back = users.get(users.size() - 1);
		assertFalse(back.ID.equals(""));
		assertFalse(back.friendNumber.equals(""));
	}
	
	/**
	 * This method will test the addFriends() function.
	 * This is a unit test that tests individual method functionality.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testAddFriends() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		RunDiffusion.createUsers("contacts.csv", users);
		
		User front = users.get(0);
		assertEquals(front.friendList.size(), 0);
		
		RunDiffusion.addFriends("contacts.csv", users);
		assertTrue(front.friendList.size() > 0);
	}
	
	/**
	 * This method will test the addPosts() function.
	 * This is a unit test that tests individual method functionality.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testAddPosts() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		RunDiffusion.createUsers("contacts.csv", users);
		
		User front = users.get(0);
		assertEquals(front.postList.size(), 0);
		
		User back = users.get(users.size() - 1);
		assertEquals(back.postList.size(), 0);
		
		RunDiffusion.addPosts("items.csv", users);
		assertTrue(front.postList.size() > 0);
		assertTrue(back.postList.size() > 0);
	}
	
	/**
	 * This method will test the buildNodes() function.
	 * This is a unit test that tests individual method functionality.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testBuildNodes() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		ArrayList<Node> nodes = new ArrayList<Node>();
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();
		RunDiffusion.createUsers("contacts.csv", users);
		RunDiffusion.addFriends("contacts.csv", users);
		RunDiffusion.addPosts("items.csv", users);
		
		assertEquals(nodes.size(), 0);
		assertEquals(nodes2.size(), 0);
		
		RunDiffusion.buildNodes(users, nodes, nodes2);
		assertTrue(nodes.size() > 0);
		assertTrue(nodes2.size() > 0);
		
		Node nodesFront = nodes.get(0);
		assertFalse(nodesFront.ID.equals(""));
		assertFalse(nodesFront.friendId.equals(""));
		
		Node nodesBack = nodes.get(nodes.size() - 1);
		assertFalse(nodesBack.ID.equals(""));
		assertFalse(nodesBack.friendId.equals(""));
		
		Node nodes2Front = nodes.get(0);
		assertFalse(nodes2Front.ID.equals(""));
		assertFalse(nodes2Front.friendId.equals(""));
		
		Node nodes2Back = nodes.get(nodes.size() - 1);
		assertFalse(nodes2Back.ID.equals(""));
		assertFalse(nodes2Back.friendId.equals(""));
	}
	
	/**
	 * This method will test the nodesToCSV() function.
	 * This is an integration test that tests CSV output given CSV input.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testNodesToCSV() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		ArrayList<Node> nodes = new ArrayList<Node>();
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();
		RunDiffusion.createUsers("contacts.csv", users);
		RunDiffusion.addFriends("contacts.csv", users);
		RunDiffusion.addPosts("items.csv", users);
		RunDiffusion.buildNodes(users, nodes, nodes2);
		
		RunDiffusion.printNodesToCSV(nodes);
		Scanner scan = new Scanner(new File("network.csv"));
		
		String first_line = scan.nextLine();
		assertTrue(first_line.equals("userId,friendId,weight"));
		
		int numLines = 1;
		while(scan.hasNextLine()) {
			scan.nextLine();
			numLines++;
		}
		assertTrue(numLines > 1);
		scan.close();
	}
	
	/**
	 * This method will test the nodes2ToCSV() function.
	 * This is an integration test that tests CSV output given CSV input.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testNodes2ToCSV() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		ArrayList<Node> nodes = new ArrayList<Node>();
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();
		RunDiffusion.createUsers("contacts.csv", users);
		RunDiffusion.addFriends("contacts.csv", users);
		RunDiffusion.addPosts("items.csv", users);
		RunDiffusion.buildNodes(users, nodes, nodes2);
		
		RunDiffusion.printNodes2ToCSV(nodes2);
		Scanner scan = new Scanner(new File("network.csv"));
		
		String first_line = scan.nextLine();
		assertTrue(first_line.equals("userId,friendId,weight"));
		
		int numLines = 1;
		while(scan.hasNextLine()) {
			scan.nextLine();
			numLines++;
		}
		assertTrue(numLines > 1);
		scan.close();
	}
	
	/**
	 * This method will test the printLatticeToCSV() function.
	 * This is an integration test that tests CSV output given CSV input.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testPrintLatticeToCSV() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		ArrayList<Node> nodes = new ArrayList<Node>();
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();
		RunDiffusion.createUsers("contacts.csv", users);
		RunDiffusion.addFriends("contacts.csv", users);
		RunDiffusion.addPosts("items.csv", users);
		RunDiffusion.buildNodes(users, nodes, nodes2);
		
		RunDiffusion.printLatticeToCSV(nodes2);
		Scanner scan = new Scanner(new File("lattice_network.csv"));
		
		String first_line = scan.nextLine();
		assertTrue(first_line.equals("userId,friendId,weight"));
		
		int numLines = 1;
		while(scan.hasNextLine()) {
			String[] line = scan.nextLine().split(",");
			int id = Integer.parseInt(line[0].substring(1));
			assertTrue(id >= 4001 && id <= 4128);
			numLines++;
		}
		assertTrue(numLines > 1);
		scan.close();
	}
	
	/**
	 * This method will test the printSmallWorldToCSV() function.
	 * This is an integration test that tests CSV output given CSV input.
	 * 
	 * @throws IOException
	 * @throws ParseException
	 */
	public void testPrintSmallWorldToCSV() throws IOException, ParseException {
		ArrayList<User> users = new ArrayList<User>();
		ArrayList<Node> nodes = new ArrayList<Node>();
		ArrayList<Node2> nodes2 = new ArrayList<Node2>();
		RunDiffusion.createUsers("contacts.csv", users);
		RunDiffusion.addFriends("contacts.csv", users);
		RunDiffusion.addPosts("items.csv", users);
		RunDiffusion.buildNodes(users, nodes, nodes2);
		
		RunDiffusion.printSmallWorldToCSV(nodes2);
		Scanner scan = new Scanner(new File("smallWorld_network.csv"));
		
		String first_line = scan.nextLine();
		assertTrue(first_line.equals("userId,friendId,weight"));
		
		int numLines = 1;
		while(scan.hasNextLine()) {
			String[] line = scan.nextLine().split(",");
			int id = Integer.parseInt(line[0].substring(1));
			assertTrue(id >= 4129 && id <= 4256);
			numLines++;
		}
		assertTrue(numLines > 1);
		scan.close();
	}
}
