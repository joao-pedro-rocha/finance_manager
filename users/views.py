from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request):
    # user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        print('HEY')

    # context = {
    #     'form': form
    # }

    return render(request, 'users/profile.html', locals())


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change_form.html'


class CustomPasswordChangeDoneView(PasswordChangeDoneView):

    def get(self, request, *args, **kwargs):
        return redirect('expenses_list')
