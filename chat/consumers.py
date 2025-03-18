# 5 шаг добавляем консумер
# consumers - это аналог view только для сокетов

# from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

# class JoinAndLeave(WebsocketConsumer):

#     # Вызывается когад клиент пытается установить соединение здесь пишем логику присоединения 
#     def connect(self):
#         print("Server say connect")
#         # должны обязательно вызвать accept() чтоб подтвердить соединение 
#         self.accept()

#     # Этот метод вызывается всякий раз, когда сервер получает сообщение от клиента через WebSocket. 
#     def receive(self, text_data=None, bytes_data=None):
#         print("Server says client message reiceved: ", text_data)
#         self.send("Server sends Welcome ") # метод send() отправляет ответ клиенту 

#     # Этот метод вызывается, когда WebSocket-соединение закрывается. Это может быть связано с тем, что клиент закрыл соединение или произошла ошибка.
#     def disconnect(self, close):
#         print("Server says disconnect")


# Простой сокет отправляющий 99 чисел клиенту
# from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# import time, asyncio

# class JoinAndLeave(AsyncWebsocketConsumer):

#     async def connect(self):
#         await self.accept()
#         for i in range(1, 100):
#             await self.send(f"Клиент держи число {i}")
#             await asyncio.sleep(1)


import json, asyncio
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer 
from accounts.models import User 
from .models import Group, Message, Event 

from channels.layers import channel_layers
from channels.db import database_sync_to_async

class JoinAndLeave(WebsocketConsumer):
    
    def connect(self):
        self.user = self.scope['user']
        self.url = self.channel_name
        print(self.user, self.url)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data) # json словарь с ответам от сервера 
        type = text_data.get('type', None)
        
        if type:
            data_uuid = text_data.get('data', None)
        if type == 'leave_group':
            self.leave_group(data_uuid)
            print(type)
        if type == "join_group":
            self.join_group(data_uuid)
    
    def leave_group(self, data_uuid):
        print(data_uuid)
        group = Group.objects.get(uuid = data_uuid)
        group.remove_user_from_group(self.user)
        data = {
            'type': 'leave_group',
            'data': data_uuid,
        }
        print("sssss")
        self.send(json.dumps(data))

    def join_group(self, data_uuid):
        group = Group.objects.get(uuid = data_uuid)
        group.add_user_to_group(self.user)
        data = {
            'type' : 'join_group',
            'data' : data_uuid,
        }
        
        self.send(json.dumps(data))
        

class GroupConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_uuid = str(self.scope['url_route']['kwargs']['uuid']) 
        print(f"~~~~~~~~~~~~~~~{self.group_uuid}")
        self.group = await database_sync_to_async(Group.objects.get)(uuid = self.group_uuid)
        await self.channel_layer.group_add(self.group_uuid, self.channel_name)

        self.user = self.scope['user']
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None): 
        text_data = json.loads(text_data)
        type = text_data.get("type", None)
        message = text_data.get('message', None)
        author = text_data.get('author', None)
        if type == 'text_message':
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + message)
            user = await database_sync_to_async(User.objects.get)(email = author)
            message = await database_sync_to_async(Message.objects.create)(author = user, content = message, group = self.group)
        await self.channel_layer.group_send(self.group_uuid, {'type': 'text_message', 'message': str(message), 'author': author})

    async def event_message(self, event):
        message = event.get("message")
        user = event.get("user", None)

        await self.send(json.dumps({'type': 'event_message', 'message': message, 'status': event.get('status', None), 'user': user}))


    async def text_message(self, event):
        message = event['message']
        author = event.get('author')

        returned_data = {'type': 'text_message!', 'message': message, 'group_uuid': self.group_uuid}
        await self.send(json.dumps(returned_data))



