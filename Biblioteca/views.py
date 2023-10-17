from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def listar_libros(request):
    libros= Libro.objects.select_related('biblioteca').prefetch_related('autores')#variable libros = clase libro y su relacion con biblioteca y autores
    #se usa select_related con relaciones 1-n y prefetch_related con relaciones n-m
    #Libro.objects es un queryset que obtiene todos los datos de los objetos Libro(como usar Libro.objects.all(()))
    return render(request,'libro/lista.html',{'libros_mostrar':libros})
#request hace referencia a la solicitud que se recibe
#libro/lista.html es el archivo que está en templates/libro/lista
#{libros_mostrar:libros} es un diccionario, la key sirve para listar los elementos de la clase libro y acceder a sus values

