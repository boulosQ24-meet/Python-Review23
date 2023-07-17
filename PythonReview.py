def create_youtube_video(title, description):
	return {
        'title': title,
        'description': description,
        'likes': 0,
        'dislikes': 0,
        'comments': {}
    }
def like (yt_video):
	if 'likes' in yt_video:
		yt_video['likes'] += 1
		return yt_video

def dislike(yt_video):
    if 'dislikes' in yt_video:
        yt_video['dislikes'] += 1
    return yt_video

def add_comment(yt_video, username, comment_text):
    if 'comments' in yt_video:
        yt_video['comments'][username] = comment_text
    return yt_video

new_video = create_youtube_video("Awesome Tutorial","test for code")

print("Videos:", new_video)


add_comment(new_video, "user1", "wooow")
add_comment(new_video, "user2", "coool")
dislike(new_video)
like(new_video)
dislike(new_video)

print("update:", new_video)


