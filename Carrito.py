from django.shortcuts import render,redirect
from .views import *
from .models import *
from django.contrib.auth.models import User


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = request.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, articulo):
        id = str(articulo.idTrabajo)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "id":articulo.idTrabajo,
                "nombre":articulo.nombre,
                "categoria":articulo.categoria.nombre,
                "precio":articulo.precio,
                "cantidad":1,
                "total":articulo.precio
            }
            self.actualizar()
        else:
           self.carrito[id]["cantidad"]+=1
           self.carrito[id]["total"]+=articulo.precio
           self.actualizar()
    
    def restar(self,articulo):
        id = str(articulo.idTrabajo)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["total"]-=articulo.precio
            if self.carrito[id]["cantidad"] == 0:
                self.eliminar(articulo)
        self.actualizar()


    def actualizar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self,articulo):
        id = str(articulo.idTrabajo)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.actualizar()

    def vaciar(self):
        self.session["carrito"]={}
        self.session.modified = True