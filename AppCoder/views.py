from AppCoder.models import Familiares
from winreg import REG_QWORD
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader

def inicio(request):
    familiares = Familiares.objects.all()
    contexto = {'familiares':familiares}
    return render(request, 'AppCoder/inicio.html', contexto)

def miembro_de_familia(request, pk):
    pariente = Familiares.objects.get(id=int(pk))
    contexto = {'pariente': pariente}
    return render(request, 'AppCoder/familiar.html', contexto)