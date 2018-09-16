import spotipy
import spotipy.util as util
import re
import urllib
from colorthief import ColorThief
import json
import colorsys
import webcolors

old = set()
newSong = True
dominant_color = [1, 1, 1]
col = ''
x = [1, 1, 1]


def theScript(user, scope, func, text, color):
    global b
    global old
    global newSong
    global x
    global dominant_color
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
    # dominant_color = ['','','']
    for i in range(1, 10):
        global dominant_color
        global x
        url_check = out_list[i]
        if 'image' in url_check:
            global dominant_color
            global x
            global col
            url_part = url_check.split('/image/')
            url_base = str("https://i.scdn.co/image/")
            url = str(url_base + url_part[1])
            p = set(out_list)
            if p.difference(old) == set():
                newSong = False
            else:
                newSong = True
            old = p
            # try:
            urllib.request.urlretrieve(url, "image.jpg")
            color_thief = ColorThief('image.jpg')
            dominant_color = color_thief.get_color(quality=1)
            col = get_colour_name(dominant_color)
            domCol(col)
            x = [dominant_color[0], dominant_color[1], dominant_color[2]]
            prop_color = colorsys.rgb_to_hsv(dominant_color[0], dominant_color[1], dominant_color[2])
            break

    #            except OSError:
    #                theScript(user, scope)

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
            print(text + " " + color + strcol + '.')

            # func.set_light(i, 'hue', (int(prop_color[0] * 65535)))
            # func.set_light(i, 'bri', (int(prop_color[1] * 254)))
            # func.set_light(i, 'sat', (int(prop_color[2])))


def domCol(colour):
    global strcol
    strcol = colour
    return strcol


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return closest_name