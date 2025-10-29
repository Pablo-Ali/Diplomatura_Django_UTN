from django.contrib import admin
from vistaprevia.models import Producto #importo la tabla
from vistaprevia.models import Categoria


class ProductoAdmin(admin.ModelAdmin):
    fields = ['categoria', 'fecha_publicacion', 'nombre_producto', 'imagen']

admin.site.register(Producto, ProductoAdmin) # cambiamos la forma de registrar el producto en el panel de administrador (cómo nos aparece)



#admin.site.register(Producto) #esto hace que la tabla con su crud aparezca en el panel de administrador
admin.site.register(Categoria)
