from django.shortcuts import render
from .models import Mascota

def index(request):
    mascotas = Mascota.objects.filter(estado='En adopción')
    return render(request, "mascotas/index.html", {"mascotas": mascotas})




#def index(request): #agrego un index básico para que no se rompa la aplicación 
#    return render(request, 'mascotas/index.html')