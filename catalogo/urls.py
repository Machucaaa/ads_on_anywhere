from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name='collections'),
    path('collectionview/<str:slug_de_cat>/', views.collectionview, name='collectionview'),  
    path('productview/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),    
    path('altascategoria/',views.altascategoria, name='altascategoria'),   
    path('altasproductos/',views.altasproductos, name='altasproductos'),     

    path('categorias_a_editar', views.selCategoria2edit, name='categorias_a_editar'),
    path('edit_categoria/<str:slug_de_cat>/', views.editUnaCategoria, name='edit_categoria'),      
    path('cats_prods_a_editar', views.selCat4prods2edit, name='cats4prods_a_editar'),  
    path('cat_de_prods4edit/<str:slug_de_cat>/', views.cat_de_prods4edit, name='sel_cat_de_prods_a_editar'),  
    path('producto_a_editar/<str:prod_slug>', views.producto2edit, name='producto2edit'),    

]
