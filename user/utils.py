from .models import User
from rest_framework.parsers import JSONParser

import user

def Isloggedin(request):
    if request.session.key("username"):
        try:
            user=User.objects.get(username=request.session["username"])
            return user
        
        except:
            return None
    
    else:
        return None