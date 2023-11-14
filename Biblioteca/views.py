from django.shortcuts import render
from .models import Libro
from .models import Cliente
from .models import Biblioteca
from .models import DatosCliente #lo hago con esta clase porque al tener una FK de cliente puedo acceder a los datos de ambas
from django.db.models import Q #sentencia or para un filtro de query
from django.views.defaults import page_not_found
from .forms import LibroForm
from .models import *
from django.contrib import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def listar_libros(request):
    libros= Libro.objects.all()#esta opcion funciona igual que la de select_related y prefetch_related pero es menos optima
    libros=Libro.objects.select_related('biblioteca').prefetch_related('autores')
    # #variable libros = clase libro y su relacion con biblioteca y autores
    #se usa select_related con relaciones 1-n o 1-1 y prefetch_related con relaciones n-m
    #Libro.objects es un queryset que obtiene todos los datos de los objetos Libro(como usar Libro.objects.all(()))
    return render(request,'libro/lista.html',{'libros_mostrar':libros})
#request hace referencia a la solicitud que se recibe
#libro/lista.html es el archivo que está en templates/libro/lista
#{libros_mostrar:libros} es un diccionario, la key sirve para listar los elementos de la clase libro y acceder a sus values

def devolver_libro(request,id_libro):
    libro=Libro.objects.select_related('biblioteca').prefetch_related('autores').get(id=id_libro)
    return render(request,'libro/libro.html',{'libro_mostrar':libro})

def datos_biblio(request):
    biblio=Biblioteca.objects.all()
    return render(request,'biblioteca/biblioteca.html',{'datos':biblio})#el nombre del value tiene que ser = al de la variable que accede a los objetos

def clientes_registrados(request):
    datos_cl=DatosCliente.objects.select_related('cliente')
    return render(request,'cliente/cliente.html',{'cliente_datos':datos_cl})

def dame_libro_fecha(request,anho_libro,mes_libro):
    libros=Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros=libros.filter(fecha_publicacion__year=anho_libro,fecha_publicacion__month=mes_libro)#con esta linea buscamos los libros
    #con el año y mes especificados en la url libros/lista/2023/10/ por ejemplo
    return render(request,'libro/lista.html',{'libros_mostrar':libros})

def dame_libro_idioma(request,idioma):
    libros=Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros=libros.filter(Q(idioma=idioma)|Q(idioma='ES')).order_by("-fecha_publicacion")#con esta linea buscamos los libros que estan en español o el idioma que indicamos
    #el order by por defecto es ascendente, para hacerlo descencente hay que poner - entre las comillas
    return render(request,'libro/lista.html',{'libros_mostrar':libros})

def dame_libros_biblioteca(request,id_biblioteca,texto_libro):
    libros=Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros=libros.filter(biblioteca=id_biblioteca).filter(descripcion__contains=texto_libro).order_by("-nombre")
    return render(request,'libro/lista.html',{'libros_mostrar':libros})

def dame_ultimo_cliente_libro(request,libro):
    cliente=Cliente.objects.filter(prestamo__libro=libro).order_by('-prestamo__fecha_prestamo')[:-1].get()
    return render(request,'cliente/cliente.html',{'cliente':cliente})

def libros_no_prestados(request):
    libros=Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros=libros.filter(prestamo=None)
    return render(request, 'libro/lista.html',{'libros_mostrar':libros})

def mi_error_404(request, exception=None):
    return render(request,'errores/404.html',None,None,404)

def libro_create(request):
    formulario=LibroForm()
    return render(request,'libro/create2.html',{'formulario':formulario})

