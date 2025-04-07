from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Post


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post.html", context={"post": post})