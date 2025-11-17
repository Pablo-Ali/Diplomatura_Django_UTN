from django.shortcuts import render

def index(request): #agrego un index básico para que no se rompa la aplicación
    
    return render(request, 'mascotas/index.html')