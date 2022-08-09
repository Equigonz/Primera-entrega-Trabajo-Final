from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def template_con_lista(request):
    context = {
        'lista':['tomate', 'banana', 'naranja'],
    }
    return render(request, 'template_lista.html',context=context)