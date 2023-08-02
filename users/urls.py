from django.urls import path
from .views import UserLogin, logout_user, signup, CustomPasswordResetView, \
    CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView, CustomPasswordChangeView, profile, \
    CustomPasswordChangeDoneView


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    # Password reset
    path('password_reset/', CustomPasswordResetView.as_view(),
         name='custom-password-reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(),
         name='custom-password-reset-done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='custom-password-reset-confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(),
         name='custom-password-reset-complete'),
    # Password change
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='custom-password-change'),
    path('password_change/done/', CustomPasswordChangeDoneView.as_view(),
         name='custom-password-change-done'),
]
