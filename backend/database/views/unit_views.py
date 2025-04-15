from rest_framework import viewsets, filters
from database.models import Unit
from database.serializers import UnitSerializer
from database.permissions import IsAdmin

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']
    permission_classes = [IsAdmin]