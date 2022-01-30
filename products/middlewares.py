from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from django.contrib import messages

def check_user_login(func):

    def inner(request):
        print(type(request.user))
        if request.user == AnonymousUser():
            messages.info(request, "User not logged in. Try logging in")
            return redirect('/signin')

        else:
            response = func(request)
            return response

    return inner
