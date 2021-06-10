from .models import User
from rest_framework.parsers import JSONParser
import bcrypt


def MAKE_PASSWORD(password):
    password = password.encode()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash.decode()


def CHECK_PASSWORD(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())


def get_username(USER):
    seperator = USER.rfind("@")
    if seperator != -1:
        USER = USER[0:seperator]
    return USER


def IsLoggedIn(request):
    if request.session.has_key("username"):
        try:
            user = User.objects.get(username=get_username(request.session["username"]))
            return user

        except:
            return None
    else:
        return None
