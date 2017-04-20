package diffusion;

/**
 * @author Sarah Devlin
 *
 * This class creates a Node2 object that stores the number of diffusion instances
 * for each relationship between a user and friend
 */
public class Node2 {
	String ID;  		// The ID of the user who made a post after their friend
	String friendId;	// The ID of the friend who made the post before the user
	int weight;			// The number of times the user made a post with the same title after the friend did

	/**
	 * This method constructs a Node2 object
	 * 
	 * @param iD			The ID of the user who made a post after their friend
	 * @param friendId		The ID of the friend who made the post before the user
	 * @param weight		The number of times the user made a post with the same title after the friend did
	 */
	public Node2(String iD, String friendId, int weight) {
		super();
		ID = iD;
		this.friendId = friendId;
		this.weight = weight;
	}
}
