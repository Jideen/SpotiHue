import spotipy
import spotipy.util as util


def tokenCode(usrnm, scp, names):
    global token
    global spotify
    for i in range(0, len(names) - 1):
        token = util.prompt_for_user_token(usrnm, scp, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07',
                                           client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                           redirect_uri='http://localhost/')
        spotify = spotipy.Spotify(auth=token)
