from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login as login_aut


# Create your views here.
def cerrar_sesion(request):
    categorias = Categoria.objects.all()
    repa= Reparacion.objects.filter(publicar=True).order_by("-nombre")[:3]
    logout(request)
    contexto = {'categorias':categorias,'reparaciones':repa}
    return render(request,"index.html",contexto)

def user_login(request):
    if request.method == 'POST':
        nom = request.POST.get("txtEmail")
        con = request.POST.get("pwdPass")
        usu = authenticate(request, username=nom, password=con)
        print(usu)
        if usu is not None and usu.is_active:
            login_aut(request,usu)
            categorias = Categoria.objects.all()
            repa= Reparacion.objects.all().order_by("-nombre")[:3]
            
            contexto = {'categorias':categorias,'reparaciones':repa}
            return render(request,"index.html",contexto)

    contexto = {'mensaje': 'Usuario/Contraseña Incorrecto'}
    return render(request, "login.html", contexto)

def index(request):
    categorias = Categoria.objects.all()
    repa= Reparacion.objects.filter(publicar=True).order_by("-nombre")[:3]
    print(repa)
    contexto = {'categorias':categorias,'reparaciones':repa}
    return render(request,"index.html",contexto)

def galeria(request):
    reparaciones= Reparacion.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    contar = Reparacion.objects.filter(publicar=True).count()
    if request.POST:
       nom = request.POST.get("txtBuscar")
       reparaciones = Reparacion.objects.filter(nombre__contains=nom)
       contar = Reparacion.objects.filter(nombre__contains=nom).count()
    contexto= {'reparaciones': reparaciones,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)

def filtro_descripcion(request):
    categorias = Categoria.objects.all()
    desc = request.POST.get("txtDesc")
    reparaciones = Reparacion.objects.filter(descripcion__contains=desc)
    contar = Reparacion.objects.filter(descripcion__contains=desc).count()
    contexto={'reparaciones':reparaciones,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)

def filtro_cate(request):
    cate = request.POST.get("cboCategoria")
    categorias = Categoria.objects.all()
    if cate=='Todos':
        reparaciones= Reparacion.objects.all()
        contar = Reparacion.objects.all().count()
    else:
        obj_cate = Categoria.objects.get(nombre=cate)
        reparaciones = Reparacion.objects.filter(categoria=obj_cate)
        contar = Reparacion.objects.filter(categoria=obj_cate).count()

    contexto={'reparaciones':reparaciones,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)

def filtro_categoria(request,id):
    cate = id
    categorias = Categoria.objects.all()
    if cate=='Todos':
        reparaciones= Reparacion.objects.all()
        contar = Reparacion.objects.all().count()
    else:
        obj_cate = Categoria.objects.get(nombre=cate)
        reparaciones = Reparacion.objects.filter(categoria=obj_cate)
        contar = Reparacion.objects.filter(categoria=obj_cate).count()
    contexto={'reparaciones':reparaciones,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto) 

def contacto(request):
    return render(request,"contacto.html")

def registrarse(request):
    contexto={'mensaje':''}
    if request.POST:
        nombre=request.POST.get("txtNombre")
        email=request.POST.get("txtEmail")
        password=request.POST.get("pwdPass")
        usu = User()
        usu.set_password(password)
        usu.username=nombre
        usu.email=email
        try:
            usu.save()
            contexto['mensaje']='Usuario registrado correctamente.'
            return render(request,"index.html",contexto)
        except:
            contexto["mensaje"]='Error al registrar usuario.'
    return render(request,"registrarse.html",contexto)



def mantenimiento(request):
    return render(request,"mantenimiento.html")


def base(request):
    return render(request,"base.html")

def agendar(request):
    return render(request,"agendar.html")


def admin_reparaciones(request):
    categorias=Categoria.objects.all()
    contexto={'categorias':categorias}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtDescripcion")
        cate = request.POST.get("cboCategoria")
        foto= request.FILES.get("txtImg")
        obj_cate = Categoria.objects.get(nombre=cate)
        rep = Reparacion(
            nombre=nombre,
            descripcion=descripcion,
            categoria=obj_cate,
            foto=foto
        )
        rep.save()
        contexto["mensaje"]="Grabo"
        return render(request,"admin_reparaciones.html",contexto)
    return render(request,"admin_reparaciones.html",contexto)

def ficha(request, nombre):
    reparacion = Reparacion.objects.get(nombre=nombre)
    data = {'reparacion': reparacion}
    return render(request,'fichas.html', data)