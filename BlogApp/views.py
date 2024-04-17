from django.shortcuts import render, redirect

from BlogApp.models import Post, Categoria


from django.contrib import messages

from .forms import PostForm, CategoriaForm

from django.shortcuts import get_object_or_404



# Create your views here.


#Post
def post(request):
    posts=Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request, "post/post.html", {"posts":posts, "categorias": categoria})


def listar_post(request):
    post = Post.objects.all()

    data = {
        'post': post
    }

    return render(request, "post/listar_post.html", data)


def agregar_post(request):

    data = {
        'form': PostForm()

    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Post creado con éxito.')
        else: 
            data["form"] = formulario
    
    return render(request, "post/agregar_post.html", data)


def modificar_post(request, id):

    post = get_object_or_404(Post, id=id)

    data= {
        'form': PostForm(instance = post)
    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST, instance=post, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Post actualizado correctamente")
            return redirect(to="listar_post")
        
        data["form"] = formulario
    
    return render(request, "post/modificar_post.html", data)


def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Post eliminado con éxito.')
    return redirect(to="listar_post")




##Categoria
def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "categoria/categoria.html", {'categorias': categoria, "posts":posts})



def listar_categoria(request):
    categoria = Categoria.objects.all()

    data = {
        'categoria': categoria
    }

    return render(request, "categoria/listar_categoria.html", data)


def modificar_categoria(request, id):

    categoria = get_object_or_404(Categoria, id=id)

    data= {
        'form': CategoriaForm(instance = categoria)
    }

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoría actualizada correctamente")
            return redirect(to="listar_categoria")
        
        data["form"] = formulario
    
    return render(request, "categoria/modificar_categoria.html", data)



def agregar_categoria(request):

    data = {
        'form': CategoriaForm()

    }

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoria creada con éxito.')
        else: 
            data["form"] = formulario
    
    return render(request, "categoria/agregar_categoria.html", data)


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, 'Categoría eliminada con éxito.')
    return redirect(to="listar_categoria")

