from canvasapi import Canvas

class userobject:
    def __init__(self, token = None):
        self._token = token
        self._API_URL = "https://csulb.instructure.com"
        print(self._token)
    
    def get_token(self) -> str:
        return self._token
    def get_url(self) -> str:
        return self._API_URL
    
    def check_token(self) -> bool:
        canvas = Canvas(self._API_URL, self._token)
        try:
            user = canvas.get_current_user()
        except:
            return False
        return True
