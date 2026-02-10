from rest_framework import serializers
from Productos.models import Productos


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
