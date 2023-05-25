
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='IND'),
    path('galeria/', galeria,name='GALE'),
    path('contacto/',contacto,name='CONTAC'),
    path('registrarse/',registrarse,name='REGI'),
    path('base/',base,name='BASE'),
    path('agendar/',agendar,name='AGENDA'),
    path('admin_reparaciones/',admin_reparaciones,name='ADM_REP'),
    path('filtro_desc/',filtro_descripcion,name='FILTRO_DESC'),
    path('filtro_categoria/<id>/',filtro_categoria,name='FILTRO_CATEGORIA'),
    path('filtro_cate/',filtro_cate,name='FILTRO_CATE'),
    path('logout/',cerrar_sesion,name='LOGOUT'),
    path('ficha/<nombre>/', ficha, name='FICHA'),
    path('login/', user_login, name='LOGIN'),
]