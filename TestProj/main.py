from cover_art import theScript as coverArt
from cover_art import newSong as ns
from Device_detection import deviceCode as detectDevice
from Device_detection import correctUserStr as cu
from Device_detection import user_nameStr as un
from Device_detection import getBool as gb
from token_check import tokenCode
from phue import Bridge
import spotipy
import spotipy.util as util
from PIL import ImageFile
from cover_art import get_colour_name as gcn
from cover_art import domCol as dc

username = ['h1z1vr98wjwqiyjfrs13bod9r', '[mag]intensity', 'user3', 'user4', 'user5']
correctUser = ['', '']
scopevals = ['user-read-playback-state,user-read-currently-playing,user-read-recently-played',
             'user-read-playback-state,user-read-currently-playing']
scope = [scopevals[0], scopevals[1], scopevals[0], scopevals[1], scopevals[0]]
token = util.prompt_for_user_token(username[0], scope[0], client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07', client_secret='7ca1f32cbf004d34a10f4000e64e83d4', redirect_uri='http://localhost/')
b = Bridge('192.168.86.22')
spotify = spotipy.Spotify(auth=token)
old = set()
user_name = ['']
updateText = str(un() + " is playing a new song on XBR-49X900E.")
strcol = ''


light_color =str("2 lights have been set to ")

def setup():
    global b
    b = Bridge('192.168.86.22')
    # b.set_light(1, 'on', True)
    # b.set_light(2, 'on', True)
    ImageFile.LOAD_TRUNCATED_IMAGES = True



def theCode():
    global spotify
    global old
    global user_name
    i = 0
#    for i in range(0, 1):
    tokenCode(username[i], scope[i],len(username))
    detectDevice(username[i], scope[i],tokenCode(username[i], scope[i],len(username)))
    if not gb():
        print("Nothing is playing on XBR-49X900E.")
    try:
        if username[i] == cu():
            updateText = str(un() + " is playing a new song on XBR-49X900E.")
            coverArt(username[i], scope[i],b,updateText,light_color)
        theCode()
    except:
        theCode()


setup()
theCode()
