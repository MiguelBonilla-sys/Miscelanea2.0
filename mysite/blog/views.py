from django.shortcuts import render
from django.utils import timezone
from blog.models import Persona, Productos, Factura, Post, Tipopersona
from blog.forms import PersonaForm, ProductosForm, FacturaForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

def post_tabla_persona(request):
    personas = Persona.objects.raw('SELECT persona.IdPersona, tipopersona.cargo AS TipodePersona, persona.TipodeDocumento, persona.Nombre, persona.Telefono, persona.Ciudad, persona.Direccion, persona.Email FROM persona INNER JOIN tipopersona ON persona.TipoPersona = tipopersona.tipo')
    Personas = {
        'personas': personas
    }
    return render(request, 'blog/post_TablaPersona.html', Personas)



def form_tabla_persona(request):
    personas_list = Persona.objects.all()
    # Coge el modelo Tipopersona pero solo el campo cargo
    tipopersonas = Tipopersona.objects.values('cargo')
    # Remplaza el campo tipopersona por el campo cargo
    for persona in personas_list:
        persona.tipopersona = persona.tipopersona.cargo
    

    ciudadBuscada = request.GET.get('ciudad')
    if ciudadBuscada:
        personas_list = personas_list.filter(ciudad=ciudadBuscada)

    tipopersonaBuscado = request.GET.get('tipopersona')
    if tipopersonaBuscado:
        personas_list = personas_list.filter(tipopersona=tipopersonaBuscado)

    idpersona = request.POST.get('idpersona')  # Cambio aquí
    if idpersona:  # Y aquí
        try:
            persona = Persona.objects.get(idpersona=idpersona)
        except Persona.DoesNotExist:
            return HttpResponse('Persona no encontrada')
        persona.tipopersona.cargo = request.POST['cargo']
        persona.tipo_de_documento = request.POST['tipodedocumento']
        persona.nombre = request.POST['nombre']
        persona.telefono = request.POST['telefono']
        persona.ciudad = request.POST['ciudad']
        persona.direccion = request.POST['direccion']
        persona.email = request.POST['email']
        persona.save()

    paginator = Paginator(personas_list,60)  # Muestra 10 personas por página

    page_number = request.GET.get('page')
    personas = paginator.get_page(page_number)

    context = {
        'form': PersonaForm(),
        'personas': personas
    }
    return render(request, 'blog/post_TablaPersona.html', context)

def post_tabla_producto(request):
    Productos ={
        'Productos': Productos.objects.all()   
    }
    return render(request, 'blog/post_TablaProducto.html', Productos)

def form_tabla_producto(request):
    productos_list = Productos.objects.all().order_by('idproductos')

    nombreBuscado = request.GET.get('nombre')
    if nombreBuscado:
        productos_list = productos_list.filter(nombre=nombreBuscado)

    idproductoBuscado = request.GET.get('idproductos')
    if idproductoBuscado:
        productos_list = productos_list.filter(idproductos=idproductoBuscado)

    idproductoEliminado = request.GET.get('idproductos')
    if idproductoEliminado:
        try:
            producto_a_eliminar = Productos.objects.get(idproductos=idproductoEliminado)
            producto_a_eliminar.delete()
        except Productos.DoesNotExist:
            pass  # manejar el error como prefieras
    paginator = Paginator(productos_list, 10)  # Muestra 10 personas por página

    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    context = {
        'form': ProductosForm(),
        'productos': productos
    }
    return render(request, 'blog/post_TablaProducto.html', context)



def post_tabla_factura(request):
    Facturas ={
        'Facturas': Factura.objects.all()   
    }
    return render(request, 'blog/post_TablaFactura.html', Facturas)

def form_tabla_factura(request):
    facturas_list = Factura.objects.all().order_by('idfactura')

    idfacturaBuscado = request.GET.get('idfactura')
    if idfacturaBuscado:
        facturas_list = facturas_list.filter(idfactura=idfacturaBuscado)

    pedidoIDpedidoBuscado = request.GET.get('pedido_idpedido')
    if pedidoIDpedidoBuscado:
        facturas_list = facturas_list.filter(pedido_idpedido=pedidoIDpedidoBuscado)

    # Necesito hacer un push de todos las variables que necesito para el formulario
    # y luego hacer un push de todas las variables que necesito para la tabla

    # Aquí creamos un diccionario con los datos necesarios para el formulario
    form_data = {
        'idfactura': request.POST.get('idfactura'),
        'productos': request.POST.get('productos'),
        'idpersona': request.POST.get('idpersona'),
        'cantidad_comprada': request.POST.get('cantidad_comprada'),
        'idpersonacli': request.POST.get('idpersonacli'),
        'pedido_idpedido': request.POST.get('pedido_idpedido'),
        'productos_idproductos': request.POST.get('productos_idproductos'),

    }

    # Creamos una instancia del formulario con los datos recibidos
    form = FacturaForm(form_data)

    # Si el formulario es válido, lo guardamos en la base de datos
    if form.is_valid():
        form.save()

    paginator = Paginator(facturas_list, 10)  # Muestra 10 personas por página

    page_number = request.GET.get('page')
    facturas = paginator.get_page(page_number)

    context = {
        'form': form,  # Pasamos el formulario al contexto
        'facturas': facturas
    }
    return render(request, 'blog/post_TablaFactura.html', context)


# Create your views here.
def post_list(request):
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
