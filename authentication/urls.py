from django.urls import path
from authentication.views import Login,Register,Logout_view

app_name = "authentication"
urlpatterns = [
    path("Login", Login, name="Login"),
    path("Register", Register, name="Register"),
    path('logout/', Logout_view, name='logout'),
    #path("Logout", Logout, name="Logout")
]