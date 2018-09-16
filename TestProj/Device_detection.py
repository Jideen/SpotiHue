import json
import spotipy

boolPlay = False
user_name=['']
def deviceCode(usrnm, scp,token):
    global correctUser
    global spotify
    global user_name
    global boolPlay
    spotify = spotipy.Spotify(auth=token)
    playback_info = spotify.current_playback('US')
    user_info = spotify.current_user()
    user_data = json.dumps(user_info)
    narrow = user_data.split('name": "')
    try:
        narrowstr = str(narrow[1])
        user_name = narrowstr.split('"')
        resultp = json.dumps(playback_info)
        filter = resultp.split('name"')
        try:
            name = str(filter[1])
            if "" in name:
                correctUser = [usrnm, scp]
                boolPlay = True
            else:
                boolPlay = False
        except IndexError:
            print("Nothing's playing.")
    except IndexError:
        print("No user present.")

def correctUserStr():
    global correctUser
    return correctUser[0]
def user_nameStr():
    global user_name
    return user_name[0]
def getBool():
    global boolPlay
    return boolPlay