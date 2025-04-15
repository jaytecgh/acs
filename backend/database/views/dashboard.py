from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from database.models import Sale, Purchase, Expense, Product

class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_sales = Sale.objects.aggregate(total=models.Sum('total_amount'))['total'] or 0
        total_purchases = Purchase.objects.aggregate(total=models.Sum('total_amount'))['total'] or 0
        total_expenses = Expense.objects.aggregate(total=models.Sum('amount'))['total'] or 0
        inventory_count = Product.objects.count()

        # Optional: monthly breakdown (last 1 months)
        from django.utils.timezone import now
        from datetime import timedelta

        monthly_sales = []
        for i in range(1):
            month = now() - timedelta(days=30 * i)
            sales = Sale.objects.filter(date__month=month.month).aggregate(total=models.Sum('total_amount'))['total'] or 0
            monthly_sales.insert(0, sales)

        return Response({
            "total_sales": total_sales,
            "total_purchases": total_purchases,
            "total_expenses": total_expenses,
            "inventory_count": inventory_count,
            "monthly_sales": monthly_sales
        })
