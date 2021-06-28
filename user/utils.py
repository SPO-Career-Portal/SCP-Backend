from .models import User
from rest_framework.parsers import JSONParser
import bcrypt
import re
import validators


def MAKE_PASSWORD(password):
    password = password.encode()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash.decode()


def CHECK_PASSWORD(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())


def linkValidator(link):
    regex = "^[https://]"
    if not re.search(regex, link):
        link = "https://" + link
    is_valid = validators.url(link)
    return is_valid


def IsLoggedIn(request):
    if request.session.has_key("username"):
        try:
            user = User.objects.get(username=request.session["username"])
            return user
        except:
            return None
    else:
        return None


def IsRegistered(request):
    try:
        data = User.objects.get(roll=request.session["roll"])
        return data.activated
    except:
        return None
