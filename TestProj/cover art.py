import spotipy
import spotipy.util as util
import re
import urllib
from colorthief import ColorThief
import json
import colorsys
from phue import Bridge
from PIL import ImageFile

# TODO: Implement multiple Spotify accounts.
# TODO: Only request info if tested user's
# TODO: Playback data indicates that the
# TODO: Playback device is Sony XBR49X900E

# TODO: Fix OSError:
# TODO: cannot identify image file 'image.jpg'

global old
old = set()


def setup():
    global b
    b = Bridge('192.168.86.22')
    b.set_light(1, 'on', True)
    b.set_light(2, 'on', True)
    ImageFile.LOAD_TRUNCATED_IMAGES = True


def theScript():
    global newSong
    global url
    global prop_color
    scope = 'user-read-currently-playing'
    token = util.prompt_for_user_token('h1z1vr98wjwqiyjfrs13bod9r', scope, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07', client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                       redirect_uri='http://localhost/')
    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.currently_playing(market='US')
    result = json.dumps(current_track)
    stuff = re.findall(r'(https?://[^\s]+)', result)
    removetable = str.maketrans('', '', '",')
    out_list = [s.translate(removetable) for s in stuff]

    for i in range(1,10):
        global old
        url_check = out_list[i]
        if 'image' in url_check:
            global newSong
            global url
            global prop_color
            url_part = url_check.split('/image/')
            url_base = str("https://i.scdn.co/image/")
            url = str(url_base+url_part[1])
            p = set(out_list)
            if p.difference(old) == set():
                newSong = False
            old = p
            urllib.request.urlretrieve(url, "image.jpg")
            color_thief = ColorThief('image.jpg')
            dominant_color = color_thief.get_color(quality=1)
            prop_color = colorsys.rgb_to_hsv(dominant_color[0], dominant_color[1], dominant_color[2])
            break
        else:
            newSong = True
    if "f0c53ef4d3" in str(url):
        b.set_light(1, 'hue', 47104)
        b.set_light(1, 'sat', 254)
        b.set_light(1, 'bri', 72)
        b.set_light(2, 'hue', 47104)
        b.set_light(2, 'sat', 254)
        b.set_light(2, 'bri', 72)
        print("But soon comes mister night.")
        theScript()
    if "83c58aeccf0f8055" in url:
        b.set_light(1, 'hue', 47104)
        b.set_light(1, 'sat', 254)
        b.set_light(1, 'bri', 72)
        b.set_light(2, 'hue', 47104)
        b.set_light(2, 'sat', 254)
        b.set_light(2, 'bri', 72)
        print("Reaching over, now his hand is on your shoulder.")
        theScript()
    if newSong:
        b.set_light(1, 'hue', (int(prop_color[0] * 65535)))
        b.set_light(1, 'bri', (int(prop_color[1] * 254)))
        b.set_light(1, 'sat', (int(prop_color[2])))
        b.set_light(2, 'hue', (int(prop_color[0] * 65535)))
        b.set_light(2, 'bri', (int(prop_color[1] * 254)))
        b.set_light(2, 'sat', (int(prop_color[2])))
        print("New song.")
        # print(b.get_api())
        theScript()
    theScript()


setup()
theScript()
