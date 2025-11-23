from django.urls import path
from inicio import views

app_name = 'mascotas'

urlpatterns = [
    path('', views.index, name='index'),
]