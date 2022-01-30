from django.urls import path
from . import views


urlpatterns = [
  path('', views.ChatApplication.as_view(), name="chat-application"),
  path('request-room/', views.RequestRoom.as_view(), name="request-room"),
  path('<str:room_name>/', views.ChatRoomName.as_view(), name="chat-room")
]
