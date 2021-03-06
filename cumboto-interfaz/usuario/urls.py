# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, patterns
from usuario.forms import LoginForm
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
#inclusión del nombre del metodo login
from usuario.views import (
	registro_usuario_view, changestatus, useractive, update_profile, acceso
   )
from . import views 

app_name = 'usuario'

urlpatterns = [
    url(r'^login/?$', 'usuario.views.acceso', name='acceso'),
	#url(r'^login/$', views.login_view, name='login'),
	url(r'^registro/$', registro_usuario_view.as_view(), name="registro"),
	url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^adminuser/$', useractive, name='adminuser'),
    url(r'^changestatus/', changestatus, name='changestatus'),
    url(r'^editar_contrasena/$', views.editar_contrasena, name='editar_contrasena'),
]
