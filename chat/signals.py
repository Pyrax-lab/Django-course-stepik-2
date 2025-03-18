from django.dispatch import receiver 
from .models import Event 
from django.db.models.signals import post_save 
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# сигнал для событий также нужно подключить в apps.py чтоб работало
@receiver(post_save, sender=Event)
def brodcast_event_to_group(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    
    group = str(instance.group.uuid)
    print(f"Signals: {group}")
    event_message = str(instance)
    async_to_sync(channel_layer.group_send)(group, {'type': 'text_message', 'message': event_message, 'status': instance.type, 'user':  str(instance.user)})