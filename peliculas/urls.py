from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pelicula/crear/', views.crear_pelicula, name='crear_pelicula'),
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('pelicula/<int:pk>/editar/', views.editar_pelicula, name='editar_pelicula'),
    path('pelicula/<int:pk>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
]