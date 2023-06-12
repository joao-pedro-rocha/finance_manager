from django.urls import path
from .views import UserLogin, logout_user, signup, CustomPasswordResetView, \
    CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('password_reset/', CustomPasswordResetView.as_view(),
         name='custom-password-reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(),
         name='custom-password-reset-done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='custom-password-reset-confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(),
         name='custom-password-reset-complete'),
]
