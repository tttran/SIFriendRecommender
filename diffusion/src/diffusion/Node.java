package diffusion;

import java.util.Date;

public class Node
{
	String ID;
	String friendId;
	String title;
	Date created;
	Date friendCreated;
	
	public void createNode(String id, String friendid, String title1, Date date1, Date friendDate1)
	{
		this.ID = id;
		this.friendId = friendid;
		this.title = title1;
		this.created = date1;
		this.friendCreated = friendDate1;
	}
}
