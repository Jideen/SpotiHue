import spotipy
from phue import Bridge
import re
import urllib
from colorthief import ColorThief
import json
import colorsys

old = set()
newSong = True
b = Bridge('192.168.86.22')
p = set()
pc = [0, 0, 114]


def getVals(yeet):
    global out_list
    token = yeet
    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.currently_playing()
    result = json.dumps(current_track)
    stuff = re.findall(r'(https?://[^\s]+)', result)
    removeTable = str.maketrans('', '', '",')
    out_list = [s.translate(removeTable) for s in stuff]
    return out_list


def theScript(data):
    global newSong
    for i in range(4, 9):
        try:
            url_check = data[i]
            if 'image' in url_check:
                url_part = url_check.split('/image/')
                url_base = str("https://i.scdn.co/image/")
                url = str(url_base + url_part[1])
                urllib.request.urlretrieve(url, "image.jpg")
                break
        except:
            print("Something's fucky...")


def colorCode():
    global prop_color
    color_thief = ColorThief('image.jpg')
    dominant_color = color_thief.get_color(quality=1)
    prop_color = colorsys.rgb_to_hsv(dominant_color[0], dominant_color[1], dominant_color[2])
    return prop_color


def newSongMath(yeet):
    global old
    global p
    p = set(getVals(yeet))
    if p.difference(old) == set():
        newSong = False
    else:
        newSong = True
    old = p
    return newSong


def theLights(colors):
    b = Bridge('192.168.86.22')
    global prop_color
    prop_color = colors
    b.set_light([1, 2], 'hue', (int(prop_color[0] * 65535)))
    b.set_light([1, 2], 'bri', (int(prop_color[1] * 254)))
    b.set_light([1, 2], 'sat', (int(prop_color[2])))
    print("Lights set.")
