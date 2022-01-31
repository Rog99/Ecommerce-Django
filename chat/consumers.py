import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Connections
from asgiref.sync import sync_to_async
from django.contrib.auth.models import AnonymousUser
from authentication.models import CustomUser


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        self.room_name = ""
        self.room_group_name = ""

    async def connect(self):
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'chat_%s' % self.room_name

            if self.scope['user'] == AnonymousUser():
                raise CustomUser.DoesNotExist('User does not exist')

            connection = await sync_to_async(Connections.objects.get, thread_sensitive=True)(room_id=self.room_name)

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

        except Connections.DoesNotExist:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

        except CustomUser.DoesNotExist:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        print("chat_message " + message)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
