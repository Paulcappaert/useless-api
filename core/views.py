from django.shortcuts import render
from django.http import HttpResponse
import time

def api(request):
    time.sleep(5)
    return HttpResponse('piss off')
