from django.contrib import admin
from vistaprevia.models import Producto #importo la tabla
from vistaprevia.models import Categoria


class ProductoAdmin(admin.ModelAdmin): # cambiamos la forma de registrar el producto en el panel de administrador (cómo nos aparece)
    #fields = ['categoria', 'fecha_publicacion', 'nombre_producto', 'imagen']
    fieldsets = [ # nos permite separar el panel en campos
        ("Relación", {"fields": ["categoria"]}), # cada tupla es una sección cuyos datos están en el diccionario
        (
            "Datos generales",
            {
                "fields": [
                    'fecha_publicacion', 'nombre_producto', 'imagen', 'estado'
                ]
            },
        ),
    ]
    list_display = ['nombre_producto', 'fecha_publicacion', 'estado', 'imagen'] # permite una mejor visualización de los datos. Pisa el método __str__ de la clase Producto
    ordering = ['-fecha_publicacion'] # ordena por fecha de más reciente a más antiguo (para cambiarlo sacamos el '-')
    list_filter = ('nombre_producto', 'fecha_publicacion',) # nos permite filtrar según esos campos
    search_fields = ('nombre_producto', 'estado',) # nos permite realizar búsquedas según esos campos
    list_display_links = ('nombre_producto', 'fecha_publicacion',) # nos permite hacer click en esos campos para ingresar al producto

admin.site.register(Producto, ProductoAdmin) 



#admin.site.register(Producto) #esto hace que la tabla con su crud aparezca en el panel de administrador
admin.site.register(Categoria)
