from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

def registro(request):
    t = get_template('registro.html')
    html = t.render(Context())
    return HttpResponse(html)

def registrado(request):
    return render_to_response('registrado.html', {'nombre': request.GET['nombre'], 'mail': request.GET['mail']})
