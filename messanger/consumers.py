import asyncio
import json
import datetime
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from user.models import Userprofile
from messanger.models import Channels
from django.contrib.auth.models import User
from minus.models import MessagesMessage


class LiveuserConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def update_user_status(self, user, status):
        print('lol')
        print(user)
        print(status)
        print('fushgsa;ld')

        channel =Channels.objects.filter(user_id=user.pk).update(is_active=status)
        if channel:
            print('qqqqqqq')
            # Channels.objects.create(user=user,is_active = status)
        else:
            Channels.objects.create(user=user,is_active = status)

    async def websocket_connect(self,event):
        print('connect',event)
        print('lol')
        self.user = self.scope["user"]
        print('kek')
        print(self.user)
        print('zbc')
        print(event)
        await self.accept()
        print('hello')
        await self.update_user_status(self.user, 1)
        print('g')

        self.room_group_name = str(self.user.id)
        # self.channel_name =
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print('new grup')


    async def websocket_disconnect(self, event):
        self.user = self.scope['user']
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        self.update_user_status(self.user, 0)
        self.accept()

    async def websocket_receive(self, text_data):
        # self.accept()
        print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')

    async def chat_message(self, event):
        message = event['message']
        user = self.scope['user']
        print('live')
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user':user.id
        }))


class MessangerConsumer(AsyncWebsocketConsumer):


    @database_sync_to_async
    def create_user_message(self, sender_id, recipient_id, message):
        print('Life is good')
        user = User.objects.get(id = recipient_id)
        message = MessagesMessage.objects.create(sender_id=sender_id.id,recipient_id = user.id,body=message['text'],sent_at = datetime.datetime.now())
        print('life is better then drug')

    # @database_sync_to_async
    # def get_last_message(self)

    async def websocket_connect(self,event):
        # pass
        self.room_name = self.scope['url_route']['kwargs']['pk']
        # print('connect')
        print(self.room_name+'kek')
        self.room_group_name = self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print('i can connect to group yeah!!!')
        await self.accept()
        # await self.accept()

    async def websocket_receive(self,text_data):
        # pass
        self.recipient_id = self.scope['url_route']['kwargs']['pk']
        self.sender_id = self.scope['user']
        # print(self.sender_id.id)
        print('ploxo')
        print(text_data)
        # text_data_json = json.loads(text_data)
        print('zbc')
        message = text_data
        await self.create_user_message(self.sender_id, self.recipient_id, message)
        # print(z)
        print(message)
        print('fuck')
        # text_data_json = json.loads(text_data)

        # message = text_data_json['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # print('disconnect')

    async def chat_message(self, event):
        message = event['message']
        user = self.scope['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user':user.id
        }))
