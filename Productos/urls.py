from django.urls import path
from Productos.views.producto_view import ProductosView

urlpatterns = [
    path('lista/', ProductosView.as_view(), name='lista_productos'),
]