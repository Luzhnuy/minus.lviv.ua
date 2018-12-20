import asyncio
import json
import datetime
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from user.models import Userprofile
from minus.models import MessagesMessage


class LiveuserConsumer(WebsocketConsumer):
    # @database_sync_to_async
    def update_user_status(self, user, status):
        print('lol')
        print(user)
        print(status)
        return Userprofile.objects.filter(user_id=user.pk).update(is_user_online=status)


    def websocket_connect(self,event):
        print('connect',event)
        print('lol')
        self.user = self.scope["user"]
        print('kek')
        print(self.user)
        print('zbc')
        print(event)
        self.accept()
        print('hello')
        z = self.update_user_status(self.user, 1)
        print(z)


    def websocket_disconnect(self, event):
        self.user = self.scope['user']

        self.update_user_status(self.user, 0)
        self.accept()

    def websocket_receive(self, text_data):
        self.accept()
        print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')



class MessangerConsumer(AsyncWebsocketConsumer):


    @database_sync_to_async
    def create_user_message(self, sender_id, recipient_id, message):
        print('Life is good')
        message = MessagesMessage.objects.create(sender_id=sender_id,recipient_id = recipient_id,body=message,send_at = datetime.datetime.now())
        message.save()
        
    async def websocket_connect(self,event):
        # pass
        print('connect')
        await self.accept()

    async def websocket_receive(self,text_data):
        # pass
        self.recipient_id = self.scope['url_route']['kwargs']['pk']
        self.sender_id = self.scope['user']
        print('ploxo')
        print(text_data)
        # text_data_json = json.loads(text_data)
        print('zbc')
        message = text_data
        self.create_user_message(self.sender_id, self.recipient_id, message)
        print('norm')
        print(message)
        print('fuck')
        await self.send(text_data=json.dumps({
            'message': message
        }))


    async def websocket_disconnect(self,event):
        print('disconnect')
