package diffusion;

public class Node2
{
	String ID;
	String friendId;
	int weight;
	
	public void createNode(String id, String friendid, int weight1)
	{
		this.ID = id;
		this.friendId = friendid;
		this.weight = weight1;
	}
}
