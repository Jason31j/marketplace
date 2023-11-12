from django.urls import path

from .views import loginPage, registerPage, logoutUser, profileView, profileUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutUser, name="logout"),
    path('profile/', profileView.as_view(), name="profile"),
    path('profile/update/', profileUpdateView.as_view(), name="profile_update"),
]
