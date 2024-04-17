from django.urls import path
from usuarios.controller import authview
from usuarios.views import valencia_refa, despedida, productlistAjax, searchproduct
from usuarios.views import sisma_pv

urlpatterns = [
    path('register/', authview.register, name='register'), 
    path('para_editar_catalogo/', authview.loginpage, name='loginpage'),  

    path('product-list', productlistAjax),
    path('searchproduct', searchproduct, name='searchproduct'),

    path('logout/', authview.logoutpage, name='logout'),
    path('valencia_refa/', valencia_refa, name='valencia_refa'),
    path('sisma_pv/', sisma_pv, name='sisma_pv'),

    path('despedida/', despedida, name='despedida'),    
]
