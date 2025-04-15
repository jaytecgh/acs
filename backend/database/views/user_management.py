
from rest_framework import viewsets, filters
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from database.models import Employee
from database.serializers import UserSerializer, EmployeeSerializer
from database.permissions import IsAdmin

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('user').all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'email', 'role']
    ordering_fields = ['full_name', 'email', 'created_at']
    ordering = ['-created_at']