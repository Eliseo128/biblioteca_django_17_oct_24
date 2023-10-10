from django.contrib import admin
from .models import Biblioteca
from .models import Autor
from .models import Libro
from .models import Cliente
from .models import DatosCliente
from .models import Prestamo
# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(DatosCliente)
admin.site.register(Prestamo)