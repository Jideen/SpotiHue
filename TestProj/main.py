from cover_art import theScript as coverArt
from cover_art import newSongMath as ns
from cover_art import getVals
from cover_art import colorCode as cc
from Device_detection import deviceCode as detectDevice
from Device_detection import correctUserStr as cu
from Device_detection import user_nameStr as un
from Device_detection import getBool as gb
from Device_detection import user_tokenStr as gu
from token_check import *
from token_check import specificToken as st
from phue import Bridge
import spotipy
import spotipy.util as util
from PIL import ImageFile
from cover_art import theLights
import time

username = ['[mag]intensity', 'h1z1vr98wjwqiyjfrs13bod9r']  # h1z1vr98wjwqiyjfrs13bod9r
scope = 'user-read-playback-state,user-read-currently-playing,user-read-recently-played'  # 'user-read-playback-state,user-read-currently-playing,user-read-recently-played']
b = Bridge('192.168.86.22')
ImageFile.LOAD_TRUNCATED_IMAGES = True
testBool = False
i = 0


def theCode():
    global i
    detectDevice(username[i], scope, tokenCode(username[(i * -1) + 1], scope, len(username)), username, i,
                 username[i])  # check for xbr
    if "mag" in cu():
        print("PARKER")
        if ns(parkerToken(scope)):
            getVals(parkerToken(scope))
            print(ns(parkerToken(scope)))
            coverArt(getVals(parkerToken(scope)))
            theLights(cc())
            print("yoy")
    elif "h1z" in cu():
        # print("JAYDEN")
        if ns(jaydenToken(scope)):
            getVals(jaydenToken(scope))
            print(ns(jaydenToken(scope)))
            coverArt(getVals(jaydenToken(scope)))
            theLights(cc())
            print("yay")
    else:
        print("Hang yourself.")
    i = (i * -1) + 1
    theCode()


theCode()
