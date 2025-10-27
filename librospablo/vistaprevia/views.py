from django.shortcuts import render
from django.http import HttpResponse

'''
def index(request): # creamos una función para mostrar por pantalla un mensaje en el front
    return HttpResponse("Hola Mundo")
'''

def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    return render(request, 'vistaprevia/index.html', params) #render va a buscar la respuesta a index.html y pasa los parámetros definidos en el diccionario