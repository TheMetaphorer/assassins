# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from datetime import timedelta

from uuid import uuid4

# Create your models here.

class PlayerObject(models.Model):
    nick = models.CharField(default="Supreme assassin", max_length=32)
    player_uuid = models.CharField(max_length=36, default=str(uuid4()))
    creation_timestamp = models.DateTimeField(default=timezone.now())
    expiration_timestamp = models.DateTimeField(default=timezone.now()+timedelta(days=1))

class LobbyObject(models.Model):
    host = models.OneToOneField(PlayerObject, on_delete=models.CASCADE, related_name='host')
    players = models.ForeignKey(PlayerObject, related_name='lobby_players')
    lobby_uuid =  models.CharField(max_length=36, default=str(uuid4()))
    creation_timestamp = models.DateTimeField(default=timezone.now())
    expiration_timestamp = models.DateTimeField(default=timezone.now()+timedelta(hours=2))



class GameObject(models.Model):
    lobby = models.OneToOneField(LobbyObject, on_delete=models.CASCADE)
    is_idle = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)