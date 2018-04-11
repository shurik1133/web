from django.shortcuts import render
from django.http import HttpResponse 

def question(request, *args, **kwargs):
    return HttpResponse('OK')
