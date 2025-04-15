from rest_framework import viewsets, filters
from database.models import Supplier
from database.serializers import SupplierSerializer
from database.permissions import IsAdmin, IsOperations

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']
    permission_classes = [IsAdmin | IsOperations]
