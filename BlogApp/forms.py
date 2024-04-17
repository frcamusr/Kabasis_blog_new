from django import forms
from .models import Post, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['titulo']

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Agregar la clase 'form-control' a cada campo

            if field_name == 'titulo':
                field.widget.attrs['placeholder'] = 'Nombre de la categoria'  # Agregar un marcador de posición para el campo 'nombre'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categorias']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Agregar la clase 'form-control' a cada campo

            if field_name == 'titulo':
                field.widget.attrs['placeholder'] = 'Titulo del post'  # Agregar un marcador de posición para el campo 'nombre'
