# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def homeView(request):
    return render(request, 'home.html')

def registerView(request):        
    if request.method == 'GET':
        return render(request, 'register.html')
    
def joinGameView(request):
    pass
