from django.contrib import admin
from vistaprevia.models import Producto #importo la tabla
from vistaprevia.models import Categoria



class ProductoInline(admin.TabularInline): # nos permite agregar nuevos productos desde la categoría
    model = Producto
    extra = 0


class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]


@admin.register(Producto) # podemos registrarlo con un decorador en vez de la línea: admin.site.register(Producto, ProductoAdmin)
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
    list_display = ['nombre_producto', 'fecha_publicacion', 'estado_de_producto', 'imagen', 'upper_case_name'] # permite una mejor visualización de los datos. Pisa el método __str__ de la clase Producto
    ordering = ['-fecha_publicacion'] # ordena por fecha de más reciente a más antiguo (para cambiarlo sacamos el '-')
    list_filter = ('nombre_producto', 'fecha_publicacion',) # nos permite filtrar según esos campos
    search_fields = ('nombre_producto', 'estado',) # nos permite realizar búsquedas según esos campos
    list_display_links = ('nombre_producto', 'fecha_publicacion',) # nos permite hacer click en esos campos para ingresar al producto
    @admin.display(description='Name') #agregamos un nuevo display para el list_display con los nombres y estados del producto en mayúsculas
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.nombre_producto, obj.estado)).upper()


#admin.site.register(Producto, ProductoAdmin) 
admin.site.register(Categoria, CategoriaAdmin)

#admin.site.register(Producto) #esto hace que la tabla con su crud aparezca en el panel de administrador
#admin.site.register(Categoria)
