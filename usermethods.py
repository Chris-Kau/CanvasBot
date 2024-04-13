from canvasapi import Canvas
API_URL = "https://csulb.instructure.com"
API_TOKEN = ''
#creates canvas object


def create_user_object(tkn):
    print("USER TOKEN", tkn, type(tkn))
    canvas = Canvas(API_URL, str(tkn))
    try:
        user = canvas.get_current_user()
    except:
        return "INVALID ACCESS TOKEN"
    return user.name