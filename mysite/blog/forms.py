from django.forms import ModelForm 
from .models import Persona, Productos, Factura, Tipopersona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['idpersona', 'tipopersona', 'tipodedocumento', 'nombre', 'telefono', 'ciudad', 'direccion', 'email']

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['idproductos', 'nombre', 'precio', 'stock_idstock', 'unidad']

class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['idfactura', 'productos', 'idpersonal', 'cantidad_comprada', 'idpersonacli', 'pedido_idpedido','productos_idproductos']
class TipopersonaForm(ModelForm):
    class Meta:
        model = Tipopersona
        fields = ['idpersona','tipo', 'cargo']