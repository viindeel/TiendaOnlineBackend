from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Productos.serializers.producto_serializer import ProductoSerializer

from Productos.models import Productos


class ProductosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        productos = Productos.objects.all()
        # Ensure we pass the queryset and verify the logic
        serializer = ProductoSerializer(productos, many=True)

        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

