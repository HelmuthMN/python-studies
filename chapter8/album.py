def make_album(artist, title, number=None):
    music_album = {
        "artist": artist.title(),
        "title": title.title()
    }
    if number:
        music_album['songs number'] = number
    return (music_album)

print(make_album("michael jackson", "bad"))
print(make_album("mac demarco", "this old dog", 10))
print(make_album("tame impala", "lonerism"))
