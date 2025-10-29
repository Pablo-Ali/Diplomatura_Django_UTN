from django.db import models

#orm que me permite crear tablas a través de clases

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True) # es el nombre sin caracteres en español, como 'espanol' para el buscador de Google

    def __str__(self):
        return '%s' % self.nombre

class Producto(models.Model):
    #tupla de opciones para el estado
    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )

    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default='Borrador') # por defecto va en Borrador
    nombre_producto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="nombre_producto/%Y/%m/%d", blank=True, null=True) # se aclara que, por defecto, puede estar en blanco
    categoria = models.ManyToManyField(Categoria) # establezco la relación N a N con la tabla Categoría
    
    def __str__(self, ):
        return self.nombre_producto
    
