from re import S
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.channel_name)
        await self.channel_layer.group_add (
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['message']
        print(message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'msg': message,
            }
        )
        return await super().receive(text_data=text_data)

    async def chat_message(self, event):
        tester = event['msg']
        await self.send(text_data=json.dumps({
            'tester': tester
        }))
