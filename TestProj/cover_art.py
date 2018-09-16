import spotipy
import spotipy.util as util
import re
import urllib
from colorthief import ColorThief
import json
import colorsys


def theScript(user, scope):
    global b
    global old
    global prop_color
    token = util.prompt_for_user_token(user, scope, client_id='[YOUR_CLIENT_ID]',
                                       client_secret='[YOUR_CLIENT_SECRET]',
                                       redirect_uri='[REDIRECT_URI]')
    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.currently_playing(market='[REGION_CODE]')
    result = json.dumps(current_track)
    stuff = re.findall(r'(https?://[^\s]+)', result)
    removeTable = str.maketrans('', '', '",')
    out_list = [s.translate(removeTable) for s in stuff]
    for i in range(1, 10):
        url_check = out_list[i]
        if 'image' in url_check:
            url_part = url_check.split('/image/')
            url_base = str("https://i.scdn.co/image/")
            url = str(url_base + url_part[1])
            p = set(out_list)
            if p.difference(old) == set():
                newSong = False
            else:
                newSong = True
            old = p
            try:
                urllib.request.urlretrieve(url, "image.jpg")
                color_thief = ColorThief('image.jpg')
                dominant_color = color_thief.get_color(quality=1)
                prop_color = colorsys.rgb_to_hsv(dominant_color[0], dominant_color[1], dominant_color[2])
                break
            except OSError:
                theScript(user, scope)
    if newSong:
        for i in range(1, 100):
            try:
                b.set_light(i, 'hue', (int(prop_color[0] * 65535)))
                b.set_light(i, 'bri', (int(prop_color[1] * 254)))
                b.set_light(i, 'sat', (int(prop_color[2])))
            except:
                print("Applied to " + str((i - 1)) + " lights.")
                break
