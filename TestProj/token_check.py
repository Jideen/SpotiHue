import spotipy.util as util


def tokenCode(usrnm, scp, names):
    global token
    token = ['']
    for i in range(0, names - 1):
        token[i] = util.prompt_for_user_token(usrnm, scp, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07',
                                              client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                              redirect_uri='http://localhost/')
        return token[i]


def parkerToken(scp):
    tokenParker = util.prompt_for_user_token('[mag]intensity', scp, client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07',
                                             client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                             redirect_uri='http://localhost/')
    return tokenParker


def jaydenToken(scp):
    tokenJayden = util.prompt_for_user_token('h1z1vr98wjwqiyjfrs13bod9r', scp,
                                             client_id='1abdcc884a4c4bf9b0f6ed7b65d07e07',
                                             client_secret='7ca1f32cbf004d34a10f4000e64e83d4',
                                             redirect_uri='http://localhost/')
    return tokenJayden
