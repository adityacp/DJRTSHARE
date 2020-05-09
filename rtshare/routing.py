from django.urls import re_path, path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    #re_path(r'ws/share/(?P<room_name>\w+)/$', ChatConsumer),
    path('ws/share/<uuid:room_name>', ChatConsumer)
]
