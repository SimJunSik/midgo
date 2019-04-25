# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['session']['user_id']

        if sender == 'junsik' :
            chat = Chat.objects.create(
                sender = sender,
                receiver = self.room_name,
                room_name = self.room_group_name,
                text = message,
            )
            chat.save()

        else :
            chat = Chat.objects.create(
                sender = sender,
                receiver = 'junsik',
                room_name = self.room_group_name,
                text = message,
            )
            chat.save()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = self.scope['session']['user_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))