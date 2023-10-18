from django.shortcuts import render
from .models import Libro
from .models import Biblioteca
from .models import DatosCliente #lo hago con esta clase porque al tener una FK de cliente puedo acceder a los datos de ambas

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