from rest_framework import viewsets, filters
from database.models import Client
from database.serializers import ClientSerializer
from database.permissions import IsAdmin, IsOperations, IsSales

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    permission_classes = [IsAdmin | IsOperations | IsSales]

