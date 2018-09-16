from .cover_art import theScript as coverArt
from .Device_detection import deviceCode as detectDevice
from .token_check import tokenCode
from .color_name import *
from phue import Bridge
import spotipy.util as util
from PIL import ImageFile

username = ['h1z1vr98wjwqiyjfrs13bod9r', '[mag]intensity', 'user3', 'user4', 'user5']
correctUser = ['', '']
scopevals = ['user-read-playback-state,user-read-currently-playing,user-read-recently-played',
             'user-read-playback-state,user-read-currently-playing']
scope = [scopevals[0], scopevals[1], scopevals[0], scopevals[1], scopevals[0]]
token = util.prompt_for_user_token('', '', client_id='', client_secret='', redirect_uri='')
b = Bridge('192.168.86.22')
spotify = ''
old = set()
prop_color = ['']

def setup():
    global b
    b = Bridge('192.168.86.22')
    b.set_light(1, 'on', True)
    b.set_light(2, 'on', True)
    ImageFile.LOAD_TRUNCATED_IMAGES = True


def theCode():
    for i in range(0, len(username) - 1):
        tokenCode(username[i], scope[i],len(username))
        detectDevice(username[i], scope[i])
        if username[i] in correctUser[1]:
            coverArt(username[i], scope[i])
            print("Current color: "+get_colour_name(prop_color)+".")
        theCode()
