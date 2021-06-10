from .models import User



def IsLoggedIn(request):
    try:
        user = User.objects.get(username=request.session["username"])
        return user
    except:
        return None