from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),#en vista.py coge la funcion index y la ejecuta
    path('libros/lista',views.listar_libros,name='lista_libros'),
    path('libros/<int:id_libro>/',views.devolver_libro,name='devolver_libro'),
]