import json
import spotipy

boolPlay = False
user_name = ['']
correctUser = ['', '']
hist = ['', '1']


def deviceCode(usrnm, scp, token, users, iter, usrnmv2):
    global correctUser
    global spotify
    global user_name
    global boolPlay
    global user_token
    global hist
    hist = [usrnm, scp]
    dataPool = users
    spotify = spotipy.Spotify(auth=token)
    playback_info = spotify.current_playback('US')
    user_info = spotify.current_user()
    # print(user_info)
    print(usrnm, "         ", usrnmv2)
    user_data = json.dumps(user_info)
    narrow = user_data.split('name": "')
    narrowstr = str(narrow[1])
    user_name = narrowstr.split('"')
    resultp = json.dumps(playback_info)
    filter1 = resultp.split('name"')
    try:
        name = str(filter1[1])
        if "Living" in name:
            correctUser = [usrnm, scp]
            user_token = dataPool[iter]
            boolPlay = True
        else:
            boolPlay = False
            correctUser = [usrnmv2, scp]
            user_token = dataPool[(-1 * iter) + 1]

    except IndexError:
        correctUser = [usrnm, scp]
        user_token = dataPool[iter]


def correctUserStr():
    global correctUser

    return correctUser[0]


def user_nameStr():
    global user_name
    return user_name[0]


def getBool():
    global boolPlay
    return boolPlay


def user_tokenStr():
    global user_token
    return user_token
