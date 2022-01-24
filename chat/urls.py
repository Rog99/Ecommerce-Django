from django.urls import path
from . import views


urlpatterns = [
  path('', views.ChatApplication.as_view(), name="chat-application"),
  path('<str:room_name>/', views.ChatRoomName.as_view(), name="chat-room")
]
