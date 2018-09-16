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
    # scope = 'user-read-currently-playing'
    token = util.prompt_for_user_token(user, scope, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07',
                                       client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                       redirect_uri='http://localhost/')
    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.currently_playing(market='US')
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
            old = p
            try:
                urllib.request.urlretrieve(url, "image.jpg")
                color_thief = ColorThief('image.jpg')
                dominant_color = color_thief.get_color(quality=1)
                prop_color = colorsys.rgb_to_hsv(dominant_color[0], dominant_color[1], dominant_color[2])
                break
            except OSError:
                theScript(user, scope)
        else:
            newSong = True
    if "f0c53ef4d3" in str(url):
        for i in range(1, 2):
            b.set_light(i, 'hue', 47104)
            b.set_light(i, 'sat', 254)
            b.set_light(i, 'bri', 72)
        print("But soon comes mister night.")
    if "83c58aeccf0f8055" in url:
        for i in range(1, 2):
            b.set_light(i, 'hue', 47104)
            b.set_light(i, 'sat', 254)
            b.set_light(i, 'bri', 72)
        print("Reaching over, now his hand is on your shoulder.")
    if newSong:
        for i in range(1, 2):
            b.set_light(i, 'hue', (int(prop_color[0] * 65535)))
            b.set_light(i, 'bri', (int(prop_color[1] * 254)))
            b.set_light(i, 'sat', (int(prop_color[2])))
        print("New song.")
    theScript(user, scope)
