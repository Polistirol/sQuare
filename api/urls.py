from django.urls import path
from . import views

urlpatterns = [

    path("",views.square,name = "home"),
    path('posts/',views.posts, name = "posts"),
    path('users/', views.users, name = "users"),
    path("my-profile/",views.profile,name = "prof"),
    path("square/",views.square,name="square"),
    path("users/<int:id>",views.userId ,name = "personal"),
    path("bet/",views.bet,name = "bet"),
    path('posts/<int:id>',views.postId, name = "myPost"),
]
