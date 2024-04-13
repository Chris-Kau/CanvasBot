import usermethods
def get_token(user_input):
    if "settoken" in user_input.lower()[:9]:
        usermethods.API_TOKEN = user_input[9:]
        temp = usermethods.API_TOKEN
        return usermethods.create_user_object(temp)