playlists = {}

def create_playlist(username, playlist_name):
    if username not in playlists:
        playlists[username] = {}
    playlists[username][playlist_name] = []
    return f"Playlist '{playlist_name}' created for {username}"

def add_to_playlist(username, playlist_name, video_id):
    if username in playlists and playlist_name in playlists[username]:
        playlists[username][playlist_name].append(video_id)
        return f"Video {video_id} added to playlist '{playlist_name}'"
    return "Playlist not found"

create_playlist("user1", "MyFavs")
add_to_playlist("user1", "MyFavs", 1)
add_to_playlist("user1", "MyFavs", 2)
add_to_playlist("user1", "MyFavs", 3)
print(playlists)