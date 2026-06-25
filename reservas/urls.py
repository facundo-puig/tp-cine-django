from django.urls import path
from . import views

urlpatterns = [
    path('seleccionar-asientos/<int:funcion_pk>/', views.seleccionar_asientos, name='seleccionar_asientos'),
    path('seleccionar-candy/', views.seleccionar_candy, name='seleccionar_candy'),
    path('confirmar/', views.confirmar_reserva, name='confirmar_reserva'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
]