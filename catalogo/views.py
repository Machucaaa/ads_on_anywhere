from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Categoria, Producto

from .forms import FormCategoria, FormProducto
# Create your views here.



def home(request):
    return render(request, "catalogo/index.html") 

def collections(request):
    categorias=Categoria.objects.filter(esta_activa=True, propietario_id=request.user.id)

    #categorias=Categoria.objects.filter(esta_activa=True)
    context={'categorias':categorias}
    return render(request, 'catalogo/collections.html', context)

def collectionview(request, slug_de_cat):
    if(Categoria.objects.filter(slug=slug_de_cat, esta_activa=True, propietario_id=request.user.id)):
        
        productos=Producto.objects.filter(categoria__slug=slug_de_cat, esta_activo = True)
        #print( productos)
        categoria_activa=Categoria.objects.filter(slug=slug_de_cat).first()
        context={ 'productos':productos, 'categoria_activa':categoria_activa }
        return render(request, "catalogo/productos/index.html", context)
    else:
        messages.warning(request, "No hay tal categoria")
        return redirect('collections')

def selCategoria2edit(request):
    categorias=Categoria.objects.filter( propietario_id=request.user.id)
    context={'categorias':categorias}
    return render(request, 'catalogo/cats4edit.html', context)

def editUnaCategoria(request, slug_de_cat):
    cat2edit = Categoria.objects.get(slug=slug_de_cat)
    form = FormCategoria(instance=cat2edit)
    context= {'form': form }
    if request.method=='POST':
        form = FormCategoria(request.POST, request.FILES, instance=cat2edit)
        if form.is_valid():
            form.save()
            return redirect('categorias_a_editar') 

    return render(request, "catalogo/edit_una_categoria.html", context)

def selCat4prods2edit(request):
    categorias=Categoria.objects.filter( propietario_id=request.user.id)
    context={'categorias':categorias}
    return render(request, 'catalogo/cats4edit_prods.html', context)

def cat_de_prods4edit(request, slug_de_cat):
    if(Categoria.objects.filter(slug=slug_de_cat, propietario_id=request.user.id)):
        
        productos=Producto.objects.filter(categoria__slug=slug_de_cat)
        #print( productos)
        categoria_activa=Categoria.objects.filter(slug=slug_de_cat).first()
        context={ 'productos':productos, 'categoria_activa':categoria_activa }
        return render(request, "catalogo/prods4edit.html", context)
    else:
        messages.warning(request, "No hay tal categoria")
        #return redirect('collections')

def producto2edit(request, prod_slug):
    prod2edit = Producto.objects.get(slug=prod_slug)
    form = FormProducto(instance=prod2edit)
    form.fields['categoria'].queryset = Categoria.objects.filter(propietario_id=request.user.id)
    context= {'form': form }
    if request.method=='POST':
        form = FormProducto(request.POST, request.FILES, instance=prod2edit)
        if form.is_valid():
            form.save()
            return redirect('cats4prods_a_editar') 

    return render(request, 'catalogo/editar_producto.html', context)


def productview(request, cate_slug, prod_slug):
    if(Categoria.objects.filter(slug=cate_slug, esta_activa=True)):
        if(Producto.objects.filter(slug=prod_slug, esta_activo=True)):
            products=Producto.objects.filter(slug=prod_slug, esta_activo=True).first()
            context={ 'products':products }
        else:
            messages.error(request, 'No hay tal producto')
            return redirect( "collections")
    else:
        messages.warning(request, "No hay tal categoria")
        return redirect('collections')
    return render(request, 'catalogo/productos/detalle_producto.html', context)


def altascategoria(request):  
    if request.user.is_authenticated:
        if request.POST:
            form = FormCategoria(request.POST, request.FILES)
            #print(request.POST)
            nom_categoria = request.POST['nombre_categoria']
            id_propietario = request.POST['propietario']
            #print(nom_categoria)  
            cant_categorias = Categoria.objects.filter(propietario_id=id_propietario, nombre_categoria = nom_categoria).count()
            #print(cant_categorias)
            if cant_categorias > 0: 
                messages.warning(request,'Ya existe la categoria!')
            else:
                if form.is_valid:
                    form.save()
                    messages.warning(request, nom_categoria + ' guardada!')
        return render(request, 'catalogo/productos/altascategoria2.html', { 'form': FormCategoria })
    else:
        return redirect('/para_editar_catalogo')

def altasproductos(request): 
    if request.user.is_authenticated: 
        id_user_activo = request.user.id
        form = FormProducto()
        form.fields['categoria'].queryset = Categoria.objects.filter(propietario_id=request.user.id)
        if request.POST:
            nom_producto = request.POST['producto']
            id_propietario = request.POST['propietario']
            form = FormProducto(request.POST, request.FILES)
            #print(request.POST)  
            cant_prods = Producto.objects.filter(propietario_id=id_propietario, producto = nom_producto).count()
            #print(cant_categorias)
            if cant_prods > 0: 
                messages.warning(request,'Ya existe el producto!')
            else:
                filepath=request.FILES.get('product_image')
                print(filepath)
                if filepath is not None:
                    if form.is_valid:
                        form.save()
                        messages.warning(request, nom_producto + ' guardado!')
                    else:
                        messages.warning(request, ' No se pudo guardar!')
                else:
                    messages.warning(request, ' Seleccione una foto!')
            #return redirect(home)
        return render(request, 'catalogo/productos/altasproductos.html', { 'form': form } )
    else:
        return redirect('/para_editar_catalogo')
