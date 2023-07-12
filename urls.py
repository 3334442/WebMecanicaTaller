
from django.contrib import admin
from django.urls import path,include
from .views import *;

urlpatterns = [
    path('', index,name='IND'),
    path('logout', cerrarSesion,name='CERRAR'),
    path('galeria', galeria,name='GAL'),
    path('indexAdministrador', indexAdministrador,name='ADMININD'),
    path('eliminarTrabajo/<id>', eliminarTrabajo,name='ELITRA'),
    path('descripcion/<id>', descripcion,name='RED'),
    path('ModificadorPost', ModificadorPost,name='MDIF'),
    path('indexFiltro', indexFiltro,name='INFIL'),
    path('login', login,name='LOG'),
    path('registrarse', registrarse,name='REG'), 
    path('carrito', carrito,name='CAR'),
    path('formularioPrimario', formularioPrimario,name='1FORM'),
    path('galeriaFiltro', galeriaFiltro,name='GAFIL'),
    path('MecanicoPost', MecanicoPost,name='MECPO'),
    path('RemodificacionPost', RemodificacionPost,name='REPO'),
    #adminPrincipal 

    path('agregar/<id>/',agregar,name='AM'),
    path('restar/<id>/',restar,name='RESTAR'),


]

