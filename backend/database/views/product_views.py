from rest_framework import viewsets, filters
from database.models import Product
from database.serializers import ProductSerializer
from database.permissions import IsAdminOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category']
    ordering_fields = ['name', 'cost_price', 'selling_price', 'stock_quantity']
    ordering = ['name']
    permission_classes = [IsAdminOrReadOnly]
