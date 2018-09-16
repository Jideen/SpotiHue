import json




def deviceCode(usrnm, scp):
    global correctUser
    global spotify
    playback_info = spotify.current_playback('[REGION_CODE]')
    user_info = spotify.current_user()
    user_data = json.dumps(user_info)
    narrow = user_data.split('name": "')
    try:
        narrowstr = str(narrow[1])
        user_name = narrowstr.split('"')
        print(user_name[0])
        resultp = json.dumps(playback_info)
        filter = resultp.split('name"')
        try:
            name = str(filter[1])
            if "[DEVICE_NAME]" in name:
                print(user_name[0] + " is playing on [DEVICE_NAME].")
                correctUser = [usrnm, scp]
            else:
                print("Playback is not on [DEVICE_NAME]")
        except IndexError:
            print("Nothing is playing.")
    except IndexError:
        print("No user present.")
