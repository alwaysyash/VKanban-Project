from django.urls import path

from . import views
app_name = "kanban"

urlpatterns = [
        path("home/",views.home,name = "home"),
        path("kontent/<int:id>/", views.kontent, name = "kontent"),
        path("create_board/", views.create_board, name = "create_board"),
        # path("registration/",views.registration,name = "register")
        ]
