from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class JoinAndLeave(WebsocketConsumer):

    # Вызывается когад клиент пытается установить соединение здесь пишем логику присоединения 
    def connect(self):
        print("Server say connect")
        # должны обязательно вызвать accept() чтоб подтвердить соединение 

    # Этот метод вызывается всякий раз, когда сервер получает сообщение от клиента через WebSocket. 
    def receive(self, text_data=None, bytes_data=None):
        print("Server says client message reiceved: ", text_data)
        self.send("Server sends Welcome ") # метод send() отправляет ответ клиенту 

    # Этот метод вызывается, когда WebSocket-соединение закрывается. Это может быть связано с тем, что клиент закрыл соединение или произошла ошибка.
    def disconnect(self, close):
        print("Server says disconnect")