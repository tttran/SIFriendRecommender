package diffusion;

import java.util.ArrayList;

public class User {
	String ID;
	String friendNumber;
	ArrayList<User> friendList;
	ArrayList<Post> postList;
	
	public void createUser(String userId, String friendnum, ArrayList<User> friends, ArrayList<Post> posts)
	{
		this.ID = userId;
		this.friendNumber = friendnum;
		this.friendList = friends;
		this.postList = posts;
	}

	public String getFriendNumber() {
		return friendNumber;
	}

	public void setFriendNumber(String friendNumber) {
		this.friendNumber = friendNumber;
	}

	public String getID() {
		return ID;
	}

	public void setID(String iD) {
		ID = iD;
	}

	public ArrayList<User> getFriendList() {
		return friendList;
	}

	public void setFriendList(ArrayList<User> friendList) {
		this.friendList = friendList;
	}

	public ArrayList<Post> getPostList() {
		return postList;
	}

	public void setPostList(ArrayList<Post> postList) {
		this.postList = postList;
	}
	
	public void addPost(Post post) {
		this.postList.add(post);
	}
	
	public void addFriend(User friend) {
		this.friendList.add(friend);
	}
	
}
