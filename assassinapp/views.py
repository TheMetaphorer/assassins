# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from forms import *
from models import *

from uuid import uuid4

# Create your views here.

def homeView(request):
    return render(request, 'home.html')

def registerView(request, **kwargs):        
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 
                'register.html',
                {'register_form': register_form})
    if request.method == 'POST':
        ## Validate form code
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            player_uuid = str(uuid4)
            user = User.objects.create(
                        username=player_uuid,
                        password='default'
            )
            user.save()
            player = PlayerObject(
                        user=user,
                        nick=request.POST['nick'],
                        uuid=player_uuid,
            )
            player.save()
            authenticated_user = authenticate(username=user.username, password=user.password)
            login(request, user)
        return HttpResponseRedirect('/assassins')

def createLobbyView(request):
    pass

                
    
def joinGameView(request):
    pass

def obliterateNick(request, uuid=None):
    print(uuid)
    player = User.objects.get(username=uuid)
    nick_object = player.playerobject
    logout(request)
    player.delete()
    nick_object.delete()
    return HttpResponseRedirect('/assassins')
