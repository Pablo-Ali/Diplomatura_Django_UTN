from django.contrib import admin
from .models import Mascota, Especie


class MascotaInline(admin.TabularInline):
    model = Mascota
    extra = 0


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    inlines = [MascotaInline]
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["especie"]}),
        ("Datos generales", {
            "fields": [
                'nombre_mascota',
                'sexo',
                'edad',
                'estado',
                'imagen',
                'fecha_publicacion'
            ]
        }),
    ]

    list_display = [
        'nombre_mascota',
        'especie',
        'edad',
        'estado_de_mascota',
        'fecha_publicacion',
    ]

    ordering = ['-fecha_publicacion']
    list_filter = ('especie', 'estado', 'sexo')
    search_fields = ('nombre_mascota', 'estado', 'sexo')
    list_display_links = ('nombre_mascota', 'fecha_publicacion')
