from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect


class UserLogin(LoginView):
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)

    return redirect('/')
