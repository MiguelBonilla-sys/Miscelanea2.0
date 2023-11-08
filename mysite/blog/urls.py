# urls.py
from django.urls import path
from .views import post_list,post_tabla_persona,form_tabla_persona,form_tabla_producto,form_tabla_factura


urlpatterns = [
    path('', post_list, name='post_list'),
    path('tabla_persona/', form_tabla_persona, name='form_tabla_persona'),
    path('tabla_producto/', form_tabla_producto, name='form_tabla_producto'),
    path('tabla_factura/', form_tabla_factura, name='form_tabla_factura'),
]
