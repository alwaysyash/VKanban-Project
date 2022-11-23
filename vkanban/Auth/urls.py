from django.urls import path

from . import views

urlpatterns = [
        path("login/",views.Login),
        path("registration/",views.registration)
        ]
