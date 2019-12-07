import asyncio
import json
import datetime
from django.core import serializers
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from user.models import Userprofile
from messanger.models import Channels,NewMessagesChannels
from django.contrib.auth.models import User
from minus.models import MessagesMessage


class LiveuserConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def update_user_status(self, user, status):
        channel =Channels.objects.filter(user_id=user.pk).update(is_active=status)
        print(channel)
        if channel:
            print("channel")
        else:
            Channels.objects.create(user=user,is_active = status)

    @database_sync_to_async
    def update_newmessages(self,frm_user,to_user):
        new_message = NewMessagesChannels.objects.filter(frm_user=frm_user,to_user=to_user)
        if new_message:
            print("new_message")
        else:
            NewMessagesChannels.objects.create(frm_user = frm_user,to_user=to_user)


    @database_sync_to_async
    def get_newmessages(self,to_user):

        return NewMessagesChannels.objects.filter(to_user=to_user)


    async def websocket_connect(self,event):

        self.user = self.scope["user"]
        await self.accept()
        print("update_user_status")
        # if self.user:
        await self.update_user_status(self.user, 1)

        self.room_group_name = str(self.user.id)
        # self.channel_name =
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )



    async def websocket_disconnect(self, event):
        self.user = self.scope['user']
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("disconnect update_user_status")
        self.update_user_status(self.user, 0)
        self.accept()

    async def websocket_receive(self, text_data):
        # message = text_data['message']
        to_user = self.scope['url_route']['kwargs']['pk']
        frm_user = self.scope['user']


        await self.update_newmessages(frm_user,to_user)


    async def chat_message(self, event):
        # self.user = self.scope['user']

        message = event['message']
        to_user = self.scope['url_route']['kwargs']['pk']
        frm_user = self.scope['user']

        new_messages = await self.get_newmessages(to_user)

        json_data = serializers.serialize('json',new_messages)
        # Send message to WebSocket

        await self.send(text_data=json.dumps({
            'message': message,
            'user':frm_user.id,
            'json_data':json_data
        }))


class MessangerConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def create_user_message(self, sender_id, recipient_id, message):

        user = User.objects.get(id = recipient_id)
        message = MessagesMessage.objects.create(sender_id=sender_id.id,recipient_id = user.id,body=message['text'],sent_at = datetime.datetime.now())


    async def websocket_connect(self,event):
        # pass
        self.room_name = self.scope['url_route']['kwargs']['pk']
        # print('connect')

        self.room_group_name = self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        # await self.accept()

    async def websocket_receive(self,text_data):
        # pass
        self.recipient_id = self.scope['url_route']['kwargs']['pk']
        self.sender_id = self.scope['user']
        # print(self.sender_id.id)

        message = text_data
        await self.create_user_message(self.sender_id, self.recipient_id, message)
        # print(z)

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

        await self.send(text_data=json.dumps({
            'message': message,
            'user':user.id
        }))
