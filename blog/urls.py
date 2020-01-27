from django.urls import path
from .import views

urlpatterns = [
    path("",views.signin,name="Signin"),
    path("signin",views.signin,name="Signin"),
    path("register",views.register,name="Register"),
    path("signout",views.signout,name="Signout"),
    path("home",views.home,name="Home"),
    path("profile",views.profile,name="Profile"),
    path("profileview/<int:user_id>",views.profileview,name="Profileview"),
    path("pst",views.pst,name="Pst"),
]