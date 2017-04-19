package diffusion;

import java.util.Date;

public class Post {
	String ID;
	String title;
	Date created;

	
	public void createPost(String userId, String title1, Date dateCreated)
	{
		this.ID = userId;
		this.title = title1;
		this.created = dateCreated;
	}


	public String getID() {
		return ID;
	}


	public void setID(String iD) {
		ID = iD;
	}


	public String getTitle() {
		return title;
	}


	public void setTitle(String title) {
		this.title = title;
	}


	public Date getCreated() {
		return created;
	}


	public void setCreated(Date created) {
		this.created = created;
	}
	
	
}
