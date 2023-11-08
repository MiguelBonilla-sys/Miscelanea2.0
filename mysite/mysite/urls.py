"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import form_tabla_persona, form_tabla_producto, form_tabla_factura

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('post_TablaPersona/', form_tabla_persona, name='post_TablaPersona'),
    path('post_TablaProducto/', form_tabla_producto, name='post_TablaProducto'),
    path('post_TablaFactura/', form_tabla_factura, name='post_TablaFactura'),
]
