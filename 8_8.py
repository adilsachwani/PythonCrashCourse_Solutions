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

prompt1 = "Enter Artist name (press q for quit) "
prompt2 = "Enter Album title (press q for quit) "

while True:
    name = input(prompt1)

    if name =='q':
        break
    else:
        album = input(prompt2)
        if album =='q':
            break
        else:
            print(make_album(name,album))
            print("")