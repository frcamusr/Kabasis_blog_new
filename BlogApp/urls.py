from django.urls import path

from . import views


urlpatterns = [

    ##Post
    path('', views.post, name="post"),

    path('listar_post/', views.listar_post, name="listar_post"),

    path('agregar_post/', views.agregar_post, name="agregar_post"),

    path('modificar_post/<id>/', views.modificar_post, name="modificar_post"),

    path('eliminar_post/<id>/', views.eliminar_post, name="eliminar_post"),



    #Categoría
    path('categoria/<int:categoria_id>/', views.categoria, name = "categoria"),

    path('listar_categoria/', views.listar_categoria, name="listar_categoria"),

    path('agregar_categoria/', views.agregar_categoria, name="agregar_categoria"),

    path('modificar_categoria/<id>/', views.modificar_categoria, name="modificar_categoria"),

    path('eliminar_categoria/<id>/', views.eliminar_categoria, name="eliminar_categoria"),

]