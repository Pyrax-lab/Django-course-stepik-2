from django.shortcuts import render
from django.http import HttpResponseForbidden
# Create your views here.


def add_post(request):
    if request.user.has_perm("permission:add_post"): # Вот так легко можемь проверять имеет ли user разрешения ан добавления поста
        return render(request, "add_post.html")
    else:# если у пользовтеля нет доступа к добавлению постов тогда ошибка разрешения
        return HttpResponseForbidden(f"Доступ запрещен {request.user}")
        #raise PermissionError
