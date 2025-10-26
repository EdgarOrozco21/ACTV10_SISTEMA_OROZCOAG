from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('editar/<int:id_proyecto>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar/<int:id_proyecto>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyectos/<int:id_proyecto>/', views.ver_proyecto, name='ver_proyecto'),
]