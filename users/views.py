from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


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


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
