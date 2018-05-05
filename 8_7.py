def make_album(artist_name, album_title, tracks=""):
    if tracks:
        albumDictionary = {'Artist Name' : artist_name.title(),
                           'Album Title' : album_title.title(),
                           'Tracks' : tracks
                           }
    else:
        albumDictionary = {'Artist Name': artist_name.title(),
                           'Album Title': album_title.title()
                           }
    return albumDictionary

print(make_album("atif aslam","meri kahani"))
print(make_album("taylot swift","fearless",8))
print(make_album("call band","jilawatan"))