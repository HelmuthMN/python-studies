
def make_album(artist, title, number=None):
    music_album = {
        "artist": artist.title(),
        "title": title.title()
    }
    if number:
        music_album['songs number'] = number
    return (music_album)


while True:
    print("Enter 'q' to quit the program")

    artist_name = input("Tell the name of the artist: ")
    if artist_name == 'q':
        break
    album_title = input("Tell the album name: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(f"The music album is: \n {album}")

