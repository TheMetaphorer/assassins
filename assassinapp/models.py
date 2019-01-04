# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AnonymousUser

from datetime import timedelta

from uuid import uuid4

# Create your models here.

class PlayerObject(models.Model):
    user = models.OneToOneField(to=User, default=0)
    nick = models.CharField(default="Supreme assassin", max_length=32)
    uuid = models.CharField(max_length=36, default=str(uuid4()))
    creation_timestamp = models.DateTimeField(default=timezone.now())
    expiration_timestamp = models.DateTimeField(default=timezone.now()+timedelta(days=1))

    def __str__(self):
        return str(self.nick)

class LobbyObject(models.Model):
    host = models.OneToOneField(PlayerObject, on_delete=models.CASCADE, related_name='host')
    players = models.ForeignKey(PlayerObject, related_name='lobby_players')
    lobby_uuid =  models.CharField(max_length=36, default=str(uuid4()))
    creation_timestamp = models.DateTimeField(default=timezone.now())
    expiration_timestamp = models.DateTimeField(default=timezone.now()+timedelta(hours=2))
    key = models.CharField(max_length=24, null=True)



class GameObject(models.Model):
    lobby = models.OneToOneField(LobbyObject, on_delete=models.CASCADE, null=True)
    is_idle = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)