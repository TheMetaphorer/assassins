
#Configure URLs for assassins app

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'register', views.registerView, name='register'),
    url(r'^', views.homeView, name='home')
]