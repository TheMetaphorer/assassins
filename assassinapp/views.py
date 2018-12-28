# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from forms import *
from models import *

from uuid import uuid4

# Create your views here.

def homeView(request):
    return render(request, 'home.html')

def registerView(request):        
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 
                'register.html',
                {'register_form': register_form})
    if request.method == 'POST':
        ## Validate form code
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            player = PlayerObject(
                        nick=request.POST['nick'],
                        uuid=str(uuid4()),
            )
            player.save()
        return HttpResponseRedirect('/assassins')


                
    
def joinGameView(request):
    pass
