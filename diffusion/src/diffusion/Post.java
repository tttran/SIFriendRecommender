package diffusion;

import java.util.Date;

/**
 * @author Sarah Devlin
 *
 *	This class creates a post object that stores post information
 *	It should be noted that a post is automatically made on behalf 
 *  of the user each time a user participates in an activity on friendica.  
 *  These posts indicate an activity the user has done, and the date created
 *  is the time they initially clicked on the activity.  
 *  (For the queries indicated in the main method, activities included are only
 *  TES modules and News/Success stories)
 */
public class Post {
	String ID;			// The ID of the user who created the post
	String title;		// The Title of the post
	Date created;		// The date the post was created

	/**
	 * @param iD			The ID of the user who created the post
	 * @param title			The Title of the post
	 * @param created		The date the post was created
	 */
	public Post(String iD, String title, Date created) {
		super();
		ID = iD;
		this.title = title;
		this.created = created;
	}
}
