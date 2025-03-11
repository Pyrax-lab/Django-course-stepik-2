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
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import time, asyncio

# class JoinAndLeave(AsyncWebsocketConsumer):

#     async def connect(self):
#         await self.accept()
#         for i in range(1, 100):
#             await self.send(f"Клиент держи число {i}")
#             await asyncio.sleep(1)

class JoinAndLeave(AsyncWebsocketConsumer):

    async def connect(self):
        
        print("!!!!!!!!!!!!")
        print(self.scope["user"])
        await self.accept()