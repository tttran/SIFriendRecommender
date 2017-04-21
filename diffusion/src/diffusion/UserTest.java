package diffusion;

import java.util.ArrayList;

import junit.framework.TestCase;

public class UserTest extends TestCase {
	
	/**
	 * Fields for User test cases
	 */
	private User user;
	private ArrayList<User> friendList = new ArrayList<>();	// The arrayList that stores all user friends
	private ArrayList<Post> postList = new ArrayList<>();	// The arrayList that stores all posts made by the user
	
	public void setUp() {
		//String iD, String friendNumber, ArrayList<User> friendList, ArrayList<Post> postList
		user = new User("1234", "0", friendList, postList);
	}
	
	
	/**
	 * Test to ensure that the user is instantiated
	 */
	public void testConstructor() {
		assertNotNull(user);
	}
	
	/**
	 * Test to ensure that fields are the correct value user
	 */
	public void testFieldsUser() {
		assertEquals(user.ID, "1234");
		assertEquals(user.friendNumber, "0");
		assertEquals(user.friendList, friendList);
		assertEquals(user.postList, postList);
	}
	
	/**
	 * Test to ensure that a user can add a post
	 */
	public void testAddPost() {
		Post p = new Post("", "", null);
		user.addPost(p);
		assertEquals(user.postList.size(), 1);
		user.addPost(p);
		user.addPost(p);
		assertEquals(user.postList.size(), 3);
	}
	
	/**
	 * Test to ensure that a user can add a friend
	 */
	public void testAddFriend() {
		User u = new User("", "", null, null);
		user.addFriend(u);
		assertEquals(user.friendList.size(), 1);
		user.addFriend(u);
		user.addFriend(u);
		assertEquals(user.friendList.size(), 3);
	}
}
