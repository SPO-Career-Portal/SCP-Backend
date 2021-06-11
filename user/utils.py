from .models import User
from rest_framework.parsers import JSONParser
import bcrypt


def MAKE_PASSWORD(password):
    password = password.encode()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash.decode()


def CHECK_PASSWORD(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())


def IsLoggedIn(request):
    if request.session.has_key("username"):
        try:
            user = User.objects.get(
                username=request.session["username"], activated=True
            )
            return user

        except:
            return None
    else:
        return None
