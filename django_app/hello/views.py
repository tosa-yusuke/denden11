from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'message': 'all friends.',
            'data': data,
        }
    return render(request, 'hello/index.html', params)

