from django.urls import path
from report import views
from django.contrib.auth import views as auth_views
#from report.core import views as core_views


urlpatterns = [
    #path('',                            views.home,             name='home'),
    path('scrap/',                       views.scrap,            name='scrap'),
    path('records/',                     views.records,          name='records'),
    path('posts/',                       views.posts,            name='posts'),
    path('allboard/',                    views.allboard,         name='allboard'),
    path('topics/',                      views.topics,           name='topics'),
    path('login/',                       views.loginview,        name='login'),

    #path('logout/',                     auth_views.logout,      name='logout'),
    path('logout/',                      views.logout,           name='logout'),
    path('signup/',                      views.signup,           name='signup'),
    path('input/',                       views.input,            name='input'),
    path('output/',                      views.output,           name='output'),
    path('nyumbani/',                    views.nyumbani,         name='nyumbani'),
    path('base1/',                       views.base1,            name='base1'),
    path('boards/<int:pk>/newpost',      views.newtopic,         name='newtopic'),
    path('boards/<int:pk>',              views.alltopics_board,  name='alltopics_board'),
    #path('boardflani/<int:pk>/',         views.boardflani,       name='boardflani'),
    path('boards/<int:pk>/post/<int:topic_pk>',views.topicflani,       name='topicflani'),
    #url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$'

]
