from rest_framework import viewsets, filters
from database.models import InventoryLog
from database.serializers import InventoryLogSerializer
from database.permissions import IsAdmin, IsOperations

class InventoryLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product__name', 'change_type']
    ordering_fields = ['log_date', 'quantity_changed']
    ordering = ['-log_date']
    permission_classes = [IsAdmin | IsOperations]