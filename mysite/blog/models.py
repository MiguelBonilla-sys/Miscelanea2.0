# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Caja(models.Model):
    idcaja = models.IntegerField(db_column='idCaja', primary_key=True)  # Field name made lowercase. The composite primary key (idCaja, Factura_IdFactura) found, that is not supported. The first column is selected.
    factura_idfactura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='Factura_IdFactura')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caja'
        unique_together = (('idcaja', 'factura_idfactura'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Factura(models.Model):
    idfactura = models.IntegerField(db_column='IdFactura', primary_key=True)  # Field name made lowercase. The composite primary key (IdFactura, Productos_idProductos) found, that is not supported. The first column is selected.
    productos = models.CharField(db_column='Productos', max_length=45)  # Field name made lowercase.
    idpersonal = models.ForeignKey('Persona', models.DO_NOTHING, db_column='IdPersonal')  # Field name made lowercase.
    cantidad_comprada = models.CharField(db_column='Cantidad Comprada', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idpersonacli = models.ForeignKey('Persona', models.DO_NOTHING, db_column='IdPersonaCLI', related_name='factura_idpersonacli_set')  # Field name made lowercase.
    pedido_idpedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='Pedido_idPedido')  # Field name made lowercase.
    productos_idproductos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='Productos_idProductos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'
        unique_together = (('idfactura', 'productos_idproductos'),)


class Pedido(models.Model):
    idpedido = models.IntegerField(db_column='idPedido', primary_key=True)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Persona_IdPersona')  # Field name made lowercase.
    productos_idproductos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='Productos_idProductos')  # Field name made lowercase.
    preciototal = models.IntegerField(db_column='PrecioTotal')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido'


class Persona(models.Model):
    idpersona = models.IntegerField(db_column='IdPersona', primary_key=True)  # Field name made lowercase.
    tipopersona = models.ForeignKey('Tipopersona',on_delete=models.CASCADE, db_column='TipoPersona')  # Field name made lowercase.
    tipodedocumento = models.CharField(db_column='TipodeDocumento', max_length=4)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Productos(models.Model):
    idproductos = models.IntegerField(db_column='idProductos', primary_key=True)  # Field name made lowercase. The composite primary key (idProductos, Stock_idStock) found, that is not supported. The first column is selected.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=50, decimal_places=0)  # Field name made lowercase.
    stock_idstock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='Stock_idStock')  # Field name made lowercase.
    unidad = models.IntegerField(db_column='Unidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'
        unique_together = (('idproductos', 'stock_idstock'),)


class Stock(models.Model):
    idstock = models.IntegerField(db_column='idStock', primary_key=True)  # Field name made lowercase. The composite primary key (idStock, Proveedor_IdPersona) found, that is not supported. The first column is selected.
    proveedor_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Proveedor_IdPersona')  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=45)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock'
        unique_together = (('idstock', 'proveedor_idpersona'),)


class Tipopersona(models.Model):
    idpersona = models.AutoField(db_column='IdPersona', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo')  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipopersona'
