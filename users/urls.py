from django.urls import path
from .views import UserLogin, logout_user, signup


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
]
