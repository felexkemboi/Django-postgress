from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from report.core import views as core_views


urlpatterns = [
    #path('',        views.home,    name='home'),
    path('scrap/',  views.scrap,   name='scrap'),
    path('records/',views.records, name='records'),
    path('posts/',  views.posts,   name='posts'),
    path('boards/', views.boards,  name='boards'),
    path('topics/', views.topics,  name='topics'),
    path('login/',  views.loginview, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', views.signup, name='signup')

]

