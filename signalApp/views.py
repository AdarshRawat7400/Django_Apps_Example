from django.db.models import signals
from django.shortcuts import render, HttpResponse
from . import signals
# Create your views here.
def home(request):
    num  = 10/0
    return HttpResponse('Hello World!')

def customSignal(request):
    signals.notification.send(sender=None, message='Custom Signal',
                              request=request, user=request.user)   

    return HttpResponse('This is custom signal page')
