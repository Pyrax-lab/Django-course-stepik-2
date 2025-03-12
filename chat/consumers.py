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

class JoinAndLeave(WebsocketConsumer):
    
    def connect(self):
        self.user = self.scope['user']
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

