from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('blog',views.blog, name="blog"),
    path('page2', views.page2,name="page2"),
    path('cloud', views.cloud, name="cloud"),
    ]
