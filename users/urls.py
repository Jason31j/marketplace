from django.urls import path

from .views import loginPage, registerPage, logoutUser, profile

app_name = 'users'

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutUser, name="logout"),
    path('profile/', profile, name="profile"),
]
