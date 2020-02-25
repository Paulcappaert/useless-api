from django.urls import path
from . import consumers
from . import views

websocket_urlpatterns = [
    path('async/wait/', consumers.BasicHttpConsumer),
    path('sync/wait/', consumers.BadHttpConsumer),
]