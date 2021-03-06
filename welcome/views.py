import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def live(request):
    return HttpResponse(PageView.objects.count())
    #return HttpResponse(content="Internal error", status=500)

def ready(request):
    return HttpResponse(PageView.objects.count())
    #return HttpResponse(content="Internal error", status=500)
