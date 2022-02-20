from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'home'
    }
    return render(request, 'music/home.html', context)