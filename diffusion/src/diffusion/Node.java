package diffusion;

import java.util.Date;

/**
 * @author Sarah Devlin
 *
 * This class creates a Node object that stores relevant diffusion data for each
 * title and relationship where diffusion occurs.
 */
public class Node {
	String ID;    // The ID of the user who made a post after their friend
	String friendId;  // The ID of the friend who made the post before the user
	String title;	// The title of the post made
	Date created;	// The date that the User made the post
	Date friendCreated;  // The date that the friend made the post

	/**
	 * This method constructs a node object
	 * 
	 * @param iD				The ID of the user who made a post after their friend
	 * @param friendId			The ID of the friend who made the post before the user
	 * @param title				The title of the post made
	 * @param created			The date that the User made the post
	 * @param friendCreated		The date that the friend made the post
	 */
	public Node(String iD, String friendId, String title, Date created, Date friendCreated) {
		super();
		ID = iD;
		this.friendId = friendId;
		this.title = title;
		this.created = created;
		this.friendCreated = friendCreated;
	}
}
