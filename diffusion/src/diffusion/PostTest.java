package diffusion;

import junit.framework.TestCase;

public class PostTest extends TestCase {

	//Field used to test Post
	private Post post;
	
	public void setUp() {
		//String iD, String title, Date created
		post = new Post("1234", "stub", null);
	}
	/**
	 * Test to ensure that a post is instantiated
	 */
	public void testConstructor() {
		assertNotNull(post);
	}
	
	/**
	 * Test to ensure that fields are the correct value post
	 */
	public void testFieldsPost() {
		assertEquals(post.ID, "1234");
		assertEquals(post.title, "stub");
		assertEquals(post.created, null);
	}
}
