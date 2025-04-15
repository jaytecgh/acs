from rest_framework import viewsets, filters
from database.models import Expense
from database.serializers import ExpenseSerializer
from database.permissions import IsAdmin, IsAccount

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['expense_type', 'department']
    ordering_fields = ['amount', 'expense_date']
    ordering = ['-expense_date']
    permission_classes = [IsAdmin | IsAccount]

