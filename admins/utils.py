from .models import Admin


def IsLoggedIn(request):
    if request.session.has_key("username"):
        try:
            user = Admin.objects.get(username=request.session["username"])
            return user
        except:
            return None
    else:
        return None
