from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm


class UserLogin(LoginView):
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)

    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/registration.html', {'form': form})
