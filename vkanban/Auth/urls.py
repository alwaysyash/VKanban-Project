from django.urls import path

from . import views
app_name = "Auth"

urlpatterns = [
        path("login/",views.Login,name = "login"),
        path("registration/",views.registration,name = "register"),
        path("logout/",views.logout_view,name = "logout")
        ]
