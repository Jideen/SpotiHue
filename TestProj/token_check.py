import spotipy
import spotipy.util as util


def tokenCode(usrnm, scp, names):
    global token
    global spotify
    for i in range(0, len(names) - 1):
        token = util.prompt_for_user_token(usrnm, scp, client_id='[YOUR_CLIENT_ID]',
                                           client_secret='[YOUR_CLIENT_SECRET]',
                                           redirect_uri='[REDIRECT_URI]')
        spotify = spotipy.Spotify(auth=token)
