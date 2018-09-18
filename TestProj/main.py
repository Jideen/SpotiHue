from cover_art import theScript as coverArt
from cover_art import newSongMath as ns
from cover_art import getVals
from cover_art import colorCode as cc
from Device_detection import deviceCode as detectDevice
from Device_detection import correctUserStr as cu
from token_check import *
from phue import Bridge
from PIL import ImageFile
from cover_art import theLights

username = ['[mag]intensity', 'h1z1vr98wjwqiyjfrs13bod9r']  # h1z1vr98wjwqiyjfrs13bod9r
scope = 'user-read-playback-state,user-read-currently-playing,user-read-recently-played'  # 'user-read-playback-state,user-read-currently-playing,user-read-recently-played']
b = Bridge('192.168.86.22')
ImageFile.LOAD_TRUNCATED_IMAGES = True
i = 0


def theCode():
    global i
    detectDevice(username[i], scope, tokenCode(username[(i * -1) + 1], scope, len(username)), username, i,
                 username[i])  # check for xbr
    if "mag" in cu():
        if ns(parkerToken(scope)):
            getVals(parkerToken(scope))
            coverArt(getVals(parkerToken(scope)))
            theLights(cc())
    elif "h1z" in cu():
        if ns(jaydenToken(scope)):
            getVals(jaydenToken(scope))
            coverArt(getVals(jaydenToken(scope)))
            theLights(cc())
    else:
        print("Hang yourself.")
    i = (i * -1) + 1
    theCode()


theCode()
