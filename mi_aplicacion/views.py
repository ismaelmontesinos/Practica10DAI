from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import FormLibro, FormPrestamo
from .models import Libro, Prestamo
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse

# Create your views here.



def index(request):
    if request.method == "POST":
    	form = FormLibro(request.POST)
    	if(form.is_valid()):
            form.save()
            return redirect('/')
    else:
        form = FormLibro()
    return render(request, "base.html",{'form':form})


def update(request,id):
	obj = Libro.objects.get(id=id)
	form = FormLibro(instance=obj)
	if request.method == "POST":
	    form = FormLibro(request.POST, instance=obj)
	    if form.is_valid():
	        form.save()
	    return redirect("edit_libro")
	return render(request, 'update.html', {'form': form})

def delete(request,id):
    form = Libro.objects.get(id = id)
    form.delete()
    return redirect('edit_libro')


def edit_libro(request,id=None):
    libros = Libro.objects.all()
    context = {'libros': libros}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)


def prestar(request,id=None):
    libros = Libro.objects.all()
    prest = Prestamo.objects.all()
    return render(request,'prestamo.html',{'libros': libros,'prest': prest})

def pedir_prestamo(request,id):
    obj = Libro.objects.get(id=id)
    form = FormPrestamo(instance=obj)
    if request.method == "POST":
        form = FormPrestamo(request.POST)
        formLibro = FormLibro(instance=obj)
        if form.is_valid():
                post = form.save(commit=False)
                post.libro = obj
                post.fecha = timezone.now()
                postLibro = formLibro.save(commit=False)
                postLibro.prestado = True
                postLibro.veces_prestado+=1;
                postLibro.save()
                post.save()
                return redirect('prestar')

    return render(request, 'pedir_prestamo.html', {'form': form, 'libro':obj})

def devolver_prestamo(request,id):
    prest = Prestamo.objects.all()
    obj = Libro.objects.get(id=id)
    if request.method == "POST":
            for pr in prest:
                if(pr.libro.id == id):
                    pr.delete()

            obj.prestado = False
            obj.save()
            return redirect('prestar')
    return render(request,'devolver_prestamo.html',{})



def estadisticas(request):
    return render(request,'estadisticas.html', {})

def json_estadisticas(request):
    libros=Libro.objects.all().order_by('-veces_prestado')
    titulos=[]
    veces_prestados=[]
    for libro in libros:
        titulos.append(libro.titulo)
        veces_prestados.append(libro.veces_prestado)
    return JsonResponse([titulos,veces_prestados],safe=False)
