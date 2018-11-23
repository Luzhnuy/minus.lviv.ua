import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class LiveuserConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connect',event)

    async def websocket_disconnect(self, event):
        print('disconnect',event)

    async def websocket_receive(self, text_data):
        print('receive',event)
