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


admin.site.register(Producto, ProductoAdmin) 



#admin.site.register(Producto) #esto hace que la tabla con su crud aparezca en el panel de administrador
admin.site.register(Categoria)
