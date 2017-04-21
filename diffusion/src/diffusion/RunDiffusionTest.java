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
		assertTrue(front.ID.equals("u4007"));
		assertTrue(front.friendNumber.equals("2028"));
		
		User middle = users.get(users.size() / 2);
		assertTrue(middle.ID.equals("u4131"));
		assertTrue(middle.friendNumber.equals("2152"));
		
		User back = users.get(users.size() - 1);
		assertTrue(back.ID.equals("u1111"));
		assertTrue(back.friendNumber.equals("2278"));
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
		
		User middle = users.get(users.size() / 2);
		assertEquals(middle.friendList.size(), 0);
		
		User back = users.get(users.size() - 1);
		assertEquals(back.friendList.size(), 0);
		
		RunDiffusion.addFriends("contacts.csv", users);
		assertEquals(front.friendList.size(), 2);
		assertEquals(middle.friendList.size(), 2);
		assertEquals(back.friendList.size(), 0);
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
		
		User middle = users.get(users.size() / 2);
		assertEquals(middle.postList.size(), 0);
		
		User back = users.get(users.size() - 1);
		assertEquals(back.postList.size(), 0);
		
		RunDiffusion.addPosts("items.csv", users);
		assertEquals(front.postList.size(), 1);
		assertEquals(middle.postList.size(), 1);
		assertEquals(back.postList.size(), 1);
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
		assertEquals(nodes.size(), 353);
		assertEquals(nodes2.size(), 222);
		
		Node nodesFront = nodes.get(0);
		assertTrue(nodesFront.ID.equals("u4013"));
		assertTrue(nodesFront.friendId.equals("u4012"));
		
		Node nodesMiddle = nodes.get(nodes.size() / 2);
		assertTrue(nodesMiddle.ID.equals("u4152"));
		assertTrue(nodesMiddle.friendId.equals("u4149"));
		
		Node nodesBack = nodes.get(nodes.size() - 1);
		assertTrue(nodesBack.ID.equals("u4254"));
		assertTrue(nodesBack.friendId.equals("u4147"));
		
		Node nodes2Front = nodes.get(0);
		assertTrue(nodes2Front.ID.equals("u4013"));
		assertTrue(nodes2Front.friendId.equals("u4012"));
		
		Node nodes2Middle = nodes.get(nodes.size() / 2);
		assertTrue(nodes2Middle.ID.equals("u4152"));
		assertTrue(nodes2Middle.friendId.equals("u4149"));
		
		Node nodes2Back = nodes.get(nodes.size() - 1);
		assertTrue(nodes2Back.ID.equals("u4254"));
		assertTrue(nodes2Back.friendId.equals("u4147"));
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
		int numLines = 0;
		while(scan.hasNextLine()) {
			scan.nextLine();
			numLines++;
		}
		assertEquals(numLines, 223);
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
		int numLines = 0;
		while(scan.hasNextLine()) {
			scan.nextLine();
			numLines++;
		}
		assertEquals(numLines, 223);
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
		int numLines = 0;
		while(scan.hasNextLine()) {
			scan.nextLine();
			numLines++;
		}
		assertEquals(numLines, 96);
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
		int numLines = 0;
		while(scan.hasNextLine()) {
			scan.nextLine();
			numLines++;
		}
		assertEquals(numLines, 128);
		scan.close();
	}
}
