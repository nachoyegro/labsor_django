from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")




