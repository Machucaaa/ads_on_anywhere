from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Categoria, Producto
from usuarios.models import Propietario



class FormCategoria(ModelForm):
    nombre_categoria = forms.TextInput()
    propietario = forms.TextInput()
    image = forms.ImageField()
    
    class Meta:
        model = Categoria
        fields = ['nombre_categoria', 'propietario', 'esta_activa', 'image']

class FormProducto(ModelForm):

    descripcion =  forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))
    class Meta:
        model = Producto
        fields = ['categoria', 'producto', 'precio_original', 'precio', 'existencia', 'esta_activo', 'en_oferta', 'product_image', 'propietario', 'descripcion']

class FormProducto0(ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['categoria'].queryset = Categoria.objects.all()

    producto = forms.TextInput()
    precio = forms.FloatField()
    existencia = forms.FloatField()
    product_image = forms.ImageField() 
    propietario = forms.TextInput() 
    

    class Meta:
        model = Producto
        fields = ['categoria',  'producto',  'precio', 'existencia', 'product_image', 'propietario']
