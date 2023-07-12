from django.shortcuts import render,redirect
from .views import *
from .Carrito import Carrito
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_aut
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def index(request):
    trabajo= Trabajo.objects.order_by("idTrabajo")[:3]
    trabajo2= Trabajo.objects.order_by("idTrabajo")
    categoria= Categoria.objects.all()
    contexto={"trabajos":trabajo, 'trabajo2': trabajo2, "categorias": categoria}

    return render(request,"index.html", contexto)

def eliminarTebajo(request, id):
    return render(request, "eliminarTrabajo/<id>.html")


@login_required(login_url='/login')

def RemodificacionPost(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        nombreMecanico = request.POST.get("cbxMecanico")
        precio = request.POST.get("precio")
        foto = request.FILES.get("foto")
        descripcion = request.POST.get("descripcion")
        nombreCategoria = request.POST.get("cbxCategoria")
        categoria = Categoria.objects.get(nombre=nombreCategoria)
        mecanico = Mecanico.objects.get(nombre=nombreMecanico)
        cantidad = request.POST.get("cantidad")

        if foto is not None :
            accion = Trabajo(
                nombre = nombre,
                mecanico = mecanico,
                precio = precio,
                foto = foto,
                descripcion = descripcion,
                categoria = categoria,
                cantidad = cantidad
            )
        else:
            accion = Trabajo(
                nombre = nombre,
                mecanico = mecanico,
                precio = precio,
                descripcion = descripcion,
                categoria = categoria,
                cantidad = cantidad
            )
        accion.save()
    categorias= Categoria.objects.all()
    mecanicos= Mecanico.objects.all()
    trabajos= Trabajo.objects.all()
    contexto={'categorias':categorias, 'mecanicos': mecanicos, 'trabajos': trabajos}
    return render(request,"RemodificacionPost.html", contexto)

def ModificadorPost(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        nombreMecanico = request.POST.get("cbxMecanico")
        precio = request.POST.get("precio")
        foto = request.FILES.get("foto")
        descripcion = request.POST.get("descripcion")
        nombreCategoria = request.POST.get("cbxCategoria")
        categoria = Categoria.objects.get(nombre=nombreCategoria)
        mecanico = Mecanico.objects.get(nombre=nombreMecanico)
        cantidad = request.POST.get("cantidad")

        if foto is not None :
            accion = Trabajo(
                nombre = nombre,
                mecanico = mecanico,
                precio = precio,
                foto = foto,
                descripcion = descripcion,
                categoria = categoria,
                cantidad = cantidad
            )
        else:
            accion = Trabajo(
                nombre = nombre,
                mecanico = mecanico,
                precio = precio,
                descripcion = descripcion,
                categoria = categoria,
                cantidad = cantidad
            )
        accion.save()
    categorias= Categoria.objects.all()
    mecanicos= Mecanico.objects.all()
    trabajos= Trabajo.objects.all()
    contexto={'categorias':categorias, 'mecanicos': mecanicos, 'trabajos': trabajos}
    return render(request,"ModificadorPost.html", contexto)


def indexFiltro(request):
    categoria = request.POST.get("cbxCategoria")

    trabajos= Trabajo.objects.order_by("idTrabajo")[:4]
    segundoTrabajo = Trabajo.objects.filter(categoria__nombre=categoria)
    categorias= Categoria.objects.all()

    contexto={'trabajos':trabajos, 'segundoTrabajo':segundoTrabajo, 'categorias':categorias}

    return render(request,"index.html", contexto)

def galeriaFiltro(request):
    nombre = request.POST.get("txtNombre")
    mecanico = request.POST.get("txtMecanico")
    categoria = request.POST.get("cbxCategoria")

    
    categorias= Categoria.objects.all()
    trabajos = Trabajo.objects.filter(nombre__contains=nombre, mecanico__nombre__contains=mecanico, categoria__nombre__contains=categoria)

    contexto={'trabajos':trabajos, 'categorias':categorias}

    return render(request,"galeria.html", contexto)


def MecanicoPost(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        nombreMecanico = request.POST.get("cbxMecanico")
        precio = request.POST.get("precio")
        foto = request.FILES.get("foto")
        descripcion = request.POST.get("descripcion")
        nombreCategoria = request.POST.get("cbxCategoria")
        categoria = Categoria.objects.get(nombre=nombreCategoria)
        mecanico = Mecanico.objects.get(nombre=nombreMecanico)
        cantidad = request.POST.get("cantidad")

        if foto is not None :
            accion = Trabajo(
                nombre = nombre,
                mecanico = mecanico,
                precio = precio,
                foto = foto,
                descripcion = descripcion,
                categoria = categoria,
                cantidad = cantidad
            )
        else:
            accion = Trabajo(
                nombre = nombre,
                mecanico = mecanico,
                precio = precio,
                descripcion = descripcion,
                categoria = categoria,
                cantidad = cantidad
            )
        accion.save()
    categorias= Categoria.objects.all()
    mecanicos= Mecanico.objects.all()
    trabajos= Trabajo.objects.all()
    contexto={'categorias':categorias, 'mecanicos': mecanicos, 'trabajos': trabajos}
    return render(request, "MecanicoPost.html", contexto)

def cerrarSesion(request):
    logout(request)
    idTrabajo= Trabajo.objects.order_by("idTrabajo")[:3]
    contexto={"trabajos":idTrabajo}

    return render(request,"index.html", contexto)

def descripcion(request,id):
    idTrabajo= Trabajo.objects.get(idTrabajo=id)
    categoria= Categoria.objects.all()
    contexto={"trabajo":idTrabajo}
    return render(request,"descripcion.html", contexto)


def formularioPrimario(request):
    return render(request,"formularioPrimario.html")

def galeria(request):
    trabajo= Trabajo.objects.all()
    categorias= Categoria.objects.all()
    contexto={"trabajos":trabajo, "categorias": categorias}

    return render(request,"galeria.html", contexto)

def eliminarTrabajo(request, id):
    contexto={'mensaje':''}
    trabajoPost= Trabajo.objects.get(idTrabajo=id)
    categorias= Categoria.objects.all()
    mecanicos= Mecanico.objects.all()
    trabajos= Trabajo.objects.all()
    contexto={'categorias':categorias, 'mecanicos': mecanicos, 'trabajos': trabajos, 'mensaje': ''}

    try:
        trabajoPost.delete()
    except:
        contexto['mensaje']='No se realizo el trabajo seleccionado'
    return render(request,"ModificadorPost.html", contexto)

def carrito(request):
    return render(request,"carrito.html")

def indexAdministrador(request):
    return render(request,"indexAdministrador.html")


def login(request):
    contexto={"mensaje":""}
    if request.POST:
        usuario= request.POST.get("txtUser")
        pas = request.POST.get("txtPass")
        us = authenticate(request,username=usuario,password=pas)
        if us is not None and us.is_active:
            login_aut(request,us)
            idTrabajo= Trabajo.objects.order_by("idTrabajo")[:3]
            contexto={"trabajos":idTrabajo}

            return render(request,"index.html", contexto)
    contexto={"mensaje": "usuario incorrecto"}
    return render(request,"login.html", contexto)
    
def registrarse(request):
    contexto={'mensaje':''}
    if request.POST:
        usuario=request.POST.get("txtUser")
        nombre=request.POST.get("txtNombre")
        apellido=request.POST.get("txtApellido")
        password= request.POST.get("txtPass")
        email=request.POST.get("txtCorreo")
        usu = User()
        usu.email=email
        usu.first_name=nombre
        usu.last_name=apellido
        usu.username=usuario
        usu.set_password(password)
        try:
            usu.save()
            contexto['mensaje']='Usuario Guardado'
        except:
            contexto['mensaje']='usuario no Guardado'

    
    return render(request,"registrarse.html")

###################################################

def agregar(request,idTrabajo):
    carrito= Carrito(request)
    trabajo = Trabajo.objects.get(idTrabajo=idTrabajo)
    carrito.agregar(trabajo)
    return redirect('/carrito/')

def restar(request,idTrabajo):
    carrito= Carrito(request)
    trabajo = Trabajo.objects.get(idMascota=idTrabajo)
    carrito.restar(trabajo)
    return redirect('/carrito/')