
#Configure URLs for assassins app

from django.conf.urls import url
from . import views
urlpatters = [
    url(r'/register', views.registerView, name='register')
]