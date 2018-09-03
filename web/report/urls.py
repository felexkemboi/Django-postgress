from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home,  name='home'),
    path('scrap/',views.scrap,name='scrap'),
    path('records/',views.records,name='records')
]
