from django.shortcuts import render
from django.http import HttpResponse

def response(request):
    html = 'kirekhar'
    return HttpResponse(html)
