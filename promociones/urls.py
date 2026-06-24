from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_promociones, name='listado_promociones'),
    path('<int:pk>/', views.detalle_promocion, name='detalle_promocion'),
    path('crear/', views.crear_promocion, name='crear_promocion'),
    path('<int:pk>/editar/', views.editar_promocion, name='editar_promocion'),
    path('<int:pk>/eliminar/', views.eliminar_promocion, name='eliminar_promocion'),
]