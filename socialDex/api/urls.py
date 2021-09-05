from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path("",views.square,name = "home"),
    path('posts/',views.posts, name = "posts"),
    path('posts/<int:id>',views.postId, name = "myPost"),
    path('posts/<str:key>',views.posts, name = "allPosts"),    
    path('users/', views.users, name = "users"),
    path("users/<int:id>",views.userId ,name = "personal"),     
    path("users/<str:key>",views.users ,name = "allUser"),  
    path("my-profile/",views.profile,name = "prof"),
    path("square/",views.square,name="square"),
    path("bet/",views.bet,name = "bet"),
    path('my-ip',views.checkIP, name = "checkIp"),
    path('change-password',auth_views.PasswordResetView.as_view(), name = "passwordReset"),
]
