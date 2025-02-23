from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST
# Create your views here.
from django.shortcuts import get_object_or_404
from htmx.models import Books
from .forms import FormBooks

@require_http_methods(["GET"])
def book_list(request):
    book = Books.objects.all()
    form = FormBooks(auto_id=False)
    return render(request, 'base.html', {'book_list':book, 'form' : form})

@require_http_methods(['POST'])
def create_book(request):
    form = FormBooks(request.POST)
    if form.is_valid():
        book = form.save()
    return render(request, 'partial_book_detail.html', {'book': book})