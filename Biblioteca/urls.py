from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),#en vista.py coge la funcion index y la ejecuta
    path('libros/lista',views.listar_libros,name='lista_libros'),
    path('libros/<int:id_libro>/',views.devolver_libro,name='devolver_libro'),
    path('biblioteca/biblioteca',views.datos_biblio,name='datos_biblio'),#el primer elemento de la tupla es el que hay que poner en la url para que cargue
    path('cliente/cliente',views.clientes_registrados,name='clientes_registrados')#el segundo elemento es el nombre de la funcion en el archivo views.py
]