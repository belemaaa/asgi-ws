from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope['url_routes']['kwargs']['room']
        self.room_group_name = 'chat%s' % self.room

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )