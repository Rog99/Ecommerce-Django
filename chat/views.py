from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ChatApplication(TemplateView):
    def get(self, request):
        return render(request, "chat/index.html")


class ChatRoomName(TemplateView):
    def get(self, request, room_name):
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })
