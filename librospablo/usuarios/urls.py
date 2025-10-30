from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.index, name='index'), #en el path inicial (sin /algo), ejecutamos la función index de views; y la llamamos 'index' (buena práctica para más adelante)
]
