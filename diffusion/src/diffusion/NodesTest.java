package diffusion;
import java.util.Date;

import junit.framework.TestCase;

public class NodesTest extends TestCase {
	
	/**
	 * Fields used to test Node and Node2
	 */
	private Node node;
	private Node2 node2;
	public void setUp() {
		//String iD, String friendId, String title, Date created, Date friendCreated
		node = new Node("1234", "5678", "friend", null, null);
		//String iD, String friendId, int weight
		node2 = new Node2("1234", "5678", 1);
	}
	/**
	 * Test to ensure that the nodes are instantiated
	 */
	public void testConstructor() {
		assertNotNull(node);
		assertNotNull(node2);
	}
	/**
	 * Test to ensure that fields are the correct value for node
	 */
	public void testFieldsNode() {
		assertEquals(node.ID, "1234");
		assertEquals(node.friendId, "5678");
		assertEquals(node.title, "friend");
		assertEquals(node.created, null);
		assertEquals(node.friendCreated, null);
	}
	/**
	 * Test to ensure that fields are the correct value node
	 */
	public void testFieldsNode2() {
		assertEquals(node2.ID, "1234");
		assertEquals(node2.friendId, "5678");
		assertEquals(node2.weight, 1);
	}
	
}
