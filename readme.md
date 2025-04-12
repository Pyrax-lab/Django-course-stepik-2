Установить Celery И Redis 

    pip install Celery
    pip install redis
    pip install -U "celery[redis]"


Потом создаем новый файл celery.py  

    import os
    from celery import Celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
    app = Celery('publish', broker_connection_retry=False,
                broker_connection_retry_on_startup=True, )
    app.config_from_object('django.conf:settings')
    broker_connection_retry = False

    app.autodiscover_tasks()

После в settings.py add redis

    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
    BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
    CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

redis в этой связке нужен как брокер сообщений то есть как бд которые хранит очереди в памяти так как Celery их не хранит у себя 

Потом создаём task.py и записываем туда логику надо учитывать что celery работает только с легкими типом данных 

    @app.task
    def test(легкие типы данных):
        .....

        логика
    
и потом эту функциию можемь вызывать где хотим в джанге

    test.delay(...) - delay указавает на то что celery должен запустить её как асинхронную функцию 


    celery -A publish worker -P eventlet -E --loglevel=info





pip install flower