from django.urls import path

from . import views

app_name = 'rtshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_room, name='create_room'),
    path('create/<str:room_name>', views.create_room, name='create_room'),
    path('<uuid:room_id>', views.view_room, name='view_room'),
]
