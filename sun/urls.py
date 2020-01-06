from django.urls import path

from . import views

app_name='sun'

urlpatterns =[
path('',views.home , name='home'),
path('cont',views.cont , name='cont'),
path('rest', views.rest, name='rest'),

path('banq', views.banq, name='banq'),
path('lawn', views.lawn, name='lawn'),
path('room', views.room, name='room'),
path('register', views.register, name='register'),

]
