playlist = ["SongA", "SongB", "SongC", "SongD"]

song_to_move = "SongC"
new_position = 1

playlist.remove(song_to_move)
playlist.insert(new_position, song_to_move)

print(playlist)