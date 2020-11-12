from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html', context={'insert_me': 'Foo'})

def help(request):
    return render(request, 'first_app/help.html', context={'help_text': 'Help needed?'})
