from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Group
from django.contrib.auth.decorators import login_required 
# Create your views here.

def home_view(request):
    '''Главная страница, на которой перечислены все группы'''
    groups = Group.objects.all() 
    user = request.user
    return render(request, 'chat/home.html', context={"groups":groups, "user":user})

def group_chat_view(request, uuid):
    '''Представление для группы, где все сообщения и события отправляются на интерфейс'''
    group = get_object_or_404(Group, uuid=uuid)
    if request.user not in group.members.all():
        return HttpResponseForbidden("You are not in group ")
    
    messages = group.mesage_moster.all()
    events = group.event_set.all()

    group_members = group.members.all()
    message_event_list = [*messages, *events]

    return render(request, "chat/groupchat.html", context={"group_members": group_members, "message_event_list": message_event_list})