from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from products.middlewares import check_user_login
from django.utils.decorators import method_decorator
import uuid
from .models import Connections
from authentication.models import CustomUser
from django.db.models import Q

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
    @method_decorator(check_user_login)
    def post(self, request):
        seller_id = request.POST["seller_id"]
        seller = CustomUser.objects.get(id=seller_id)
        # try:
        bool_connect = Connections.objects.filter(
            (Q(user=request.user) | Q(user=seller)) & (Q(friend=request.user) | Q(friend=seller))
        ).get()
        print("line 34")
        print(bool_connect.room_id)

        return redirect('/chat/' + bool_connect.room_id)

        # except Connections.DoesNotExist:
        #     # check if the connections exists in the database
        #     room_id = uuid.uuid4().hex
        #     connection = Connections(
        #         room_id=room_id,
        #         user=request.user,
        #         friend=seller
        #     )
        #     connection.save()
        #     return redirect('/')
