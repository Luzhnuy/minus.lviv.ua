import asyncio
import json
from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from user.models import Userprofile


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
