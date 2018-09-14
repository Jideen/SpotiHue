import spotipy
import spotipy.util as util
import json



# TODO: Load spotify profiles of all users
# TODO: Check which user is casting to TV
# TODO: set cover art script to use current
# TODO: User's spotify auth token
def bigOof():
    scope = 'user-read-playback-state,user-read-currently-playing'
    token = util.prompt_for_user_token('h1z1vr98wjwqiyjfrs13bod9r', scope, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07',
                                       client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                       redirect_uri='http://localhost/')
    spotify = spotipy.Spotify(auth=token)
    playback_info = spotify.current_playback('US')
    current_track = spotify.currently_playing(market='US')
    result = json.dumps(playback_info)
    filter = result.split('name"')
    name = str(filter[1])

    if "XBR-49" in name:
        testBool = True
    else:
        testBool = False
    print(testBool)
    print(current_track)
bigOof()