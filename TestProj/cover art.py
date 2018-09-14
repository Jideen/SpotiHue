import coverpy
import spotipy
import spotipy.util as util
import re
import urllib
from colorthief import ColorThief
import json
import colorsys
from phue import Bridge
import time
import random
def theScript():
    b = Bridge('192.168.86.22')
    print("CoverPy console:")
    c = coverpy.CoverPy()
    scope = 'user-read-currently-playing'

    token = util.prompt_for_user_token('h1z1vr98wjwqiyjfrs13bod9r', scope, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07', client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                       redirect_uri='http://localhost/')

    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.currently_playing(market='US')
    result = json.dumps(current_track)
    stuff = re.findall(r'(https?://[^\s]+)', result)
    removetable = str.maketrans('', '', '",')
    out_list = [s.translate(removetable) for s in stuff]
    url = out_list[random.randint(5,8)]
    if "image" in url:
        print(url)
        urllib.request.urlretrieve(url, "image.jpg")
        color_thief = ColorThief('image.jpg')
        dominant_color = color_thief.get_color(quality=1)
        print(dominant_color)
        print("red: ",[dominant_color[0]])
        print("green: ",[dominant_color[1]])
        print("blue: ",[dominant_color[2]])
        prop_color = colorsys.rgb_to_hsv(dominant_color[0],dominant_color[1],dominant_color[2])
        print(prop_color)
        print(prop_color[2])
        print(b.get_api())
        b.set_light(1, 'hue', (int(prop_color[0]*65535)))
        b.set_light(1, 'sat', (int(prop_color[2])))
        b.set_light(1, 'bri', (int(prop_color[1]*254)))
        b.set_light(2, 'hue', (int(prop_color[0]*65535)))
        b.set_light(2, 'sat', (int(prop_color[2])))
        b.set_light(2, 'bri', (int(prop_color[1]*254)))
        print(b.get_api())
        time.sleep(20)
        theScript()
    elif "image" not in url:
        url = out_list[random.randint(5,10)]
        theScript()
theScript()
