from django.urls import path

from . import views
app_name = "kanban"

urlpatterns = [
        path("home/",views.home,name = "home"),
        path("kontent/<int:id>/", views.kontent, name = "kontent"),
        path("create_board/", views.create_board, name = "create_board"),
        path("add_card/<int:kid>/<str:state>/",views.add_card, name = "add_card"),
        path("delete_card/<int:kid>/<int:cid>/",views.delete_card, name = "delete_card"),
        path("join_board/", views.join_board, name = "join_board"),
        path("move_card/<int:kid>/<int:cid>/<str:state>/", views.move_card, name = "move_card"),
        # path("registration/",views.registration,name = "register")
        ]
