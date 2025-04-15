from rest_framework import viewsets, filters
from database.models import Admin
from database.serializers import AdminSerializer
from database.permissions import IsAdmin

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'employee__full_name', 'employee__email']
    ordering_fields = ['username', 'employee__full_name']
    ordering = ['username']
    permission_classes = [IsAdmin]

