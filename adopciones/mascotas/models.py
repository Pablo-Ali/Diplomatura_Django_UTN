from django.db import models
from django.utils.html import format_html # nos permite usar formato html

class Especie(models.Model):
    nombre = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return '%s' % self.nombre

class Mascota(models.Model):
    #tupla de opciones para el estado
    Adoptado = 'Adoptado'
    En_Adopcion = 'En adopción'
    ESTADO_MASCOTA = (
        (Adoptado, 'Adoptado'),
        (En_Adopcion, 'En adopción'),
    )

    estado = models.CharField(max_length=15, choices=ESTADO_MASCOTA, default='En adopción')
    nombre_mascota = models.CharField(max_length=200)
    sexo = models.CharField(max_length=20, default="No especificado")
    edad = models.IntegerField(default=0)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="nombre_mascota/%Y/%m/%d", blank=True, null=True)
    especie = models.ForeignKey(
        Especie, blank=False, null=True, on_delete=models.CASCADE
    )


    def estado_de_mascota(self):
        if self.estado == 'Adoptado':
            return format_html('<span style="color: #f00;">{}</span>', self.estado, )
        elif self.estado == 'En adopción':
            return format_html('<span style="color: #f0f;">{}</span>', self.estado, )
    
    
    def __str__(self, ):
        return self.nombre_mascota