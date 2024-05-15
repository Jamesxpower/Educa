import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone

#class ChatConsumer(WebsocketConsumer):
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'

        # join room group
        #async_to_sync(self.channel_layer.group_add)(
        #    self.room_group_name,
        #    self.channel_name
        #)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # accept connection
        await self.accept()

    async def disconnect(self, code):
        #async_to_sync(self.channel_layer.group_discard)(
        #    self.room_group_name,
        #    self.channel_name
        #)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # send message to WebSocket
        #self.send(text_data=json.dumps({'message': message}))

        # send message to room group
        #async_to_sync(self.channel_layer.group_send)(
        #    self.room_group_name,
        #    {
        #        'type': 'chat_message',
        #        'message': message,
        #        'user': self.user,
        #        'datetime': now.isoformat(),
        #    }
        #)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user,
                'datetime': now.isoformat(),
            }
        )


    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))
        
