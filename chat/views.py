from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class ChatApplication(TemplateView):
    def get(self, request):
        return render(request, "chat/index.html")


class ChatRoomName(TemplateView):
    def get(self, request, room_name):
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })


class RequestRoom(TemplateView):

    @method_decorator(csrf_exempt)
    def post(self, request):
        print(request.POST["name"])
        return HttpResponse("Hello World")
