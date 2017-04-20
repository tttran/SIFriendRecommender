package diffusion;

import java.util.ArrayList;

/**
 * @author Sarah Devlin
 *
 * This class creates a User object that stores relevant user data
 */
public class User {
	String ID;  				// The ID of the user
	String friendNumber;		// The number that links a user to their friends in the CSV
	ArrayList<User> friendList;	// The arrayList that stores all user friends
	ArrayList<Post> postList;	// The arrayList that stores all posts made by the user

	/**
	 * This method constructs a user instance
	 * 
	 * @param iD				The ID of the user
	 * @param friendNumber		The number that links a user to their friends in the CSV
	 * @param friendList		The arrayList that stores all user friends
	 * @param postList			The arrayList that stores all posts made by the user
	 */
	public User(String iD, String friendNumber, ArrayList<User> friendList, ArrayList<Post> postList) {
		super();
		ID = iD;
		this.friendNumber = friendNumber;
		this.friendList = friendList;
		this.postList = postList;
	}

	/**
	 * This method adds a post to the postList of a user
	 * 
	 * @param post  The post to be added
	 */
	public void addPost(Post post) {
		this.postList.add(post);  // adds the post to the postList
	}

	/**
	 * This method adds a friend to the friendList of a user
	 * 
	 * @param friend	The friend to be added
	 */
	public void addFriend(User friend) {
		this.friendList.add(friend); // adds the friend to the friendList
	}

}
