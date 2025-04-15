import pandas as pd
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse
from datetime import datetime
from io import TextIOWrapper

from database.models import (
    Report, Sale, Purchase, Payment, InventoryLog, Transport,
    Product, Supplier, Client
)
from database.serializers import ReportSerializer, ProductSerializer, SaleSerializer, PurchaseSerializer
from database.permissions import IsAdmin, IsOperations, IsSales, IsAccount

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['report_type']
    ordering_fields = ['report_date', 'total_amount']
    ordering = ['-report_date']
    permission_classes = [IsAdmin | IsOperations | IsSales | IsAccount]

    def get_date_filtered_queryset(self, model, request):
        queryset = model.objects.all()
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date:
            queryset = queryset.filter(created_at__gte=start_date)
        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset

    def export_as_excel(self, df, filename):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        df.to_excel(response, index=False)
        return response

    def export_as_csv(self, df, filename):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        df.to_csv(path_or_buf=response, index=False)
        return response

    @action(detail=False, methods=['get'])
    def export_products_csv(self, request):
        products = Product.objects.all()
        data = [
            {
                "Name": p.name,
                "Category": p.category,
                "Size": p.size,
                "Unit": p.unit.name if p.unit else '',
                "Cost Price": p.cost_price,
                "Selling Price": p.selling_price,
                "Stock Quantity": p.stock_quantity,
                "Created At": p.created_at,
            } for p in products
        ]
        df = pd.DataFrame(data)
        return self.export_as_csv(df, "products.csv")

    @action(detail=False, methods=['post'])
    def import_products_csv(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)
        df = pd.read_csv(file)
        for _, row in df.iterrows():
            Product.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'category': row.get('Category', ''),
                    'size': row.get('Size', ''),
                    'cost_price': row.get('Cost Price', 0),
                    'selling_price': row.get('Selling Price', 0),
                    'stock_quantity': row.get('Stock Quantity', 0),
                }
            )
        return Response({"status": "Products imported successfully."})

    @action(detail=False, methods=['get'])
    def export_sales_csv(self, request):
        sales = self.get_date_filtered_queryset(Sale, request)
        data = []
        for sale in sales.select_related('client').prefetch_related('saletransactions'):
            for item in sale.saletransactions.all():
                data.append({
                    "Invoice #": sale.invoice_number,
                    "Date": sale.date,
                    "Client": sale.client.name if sale.client else '',
                    "Product": item.product.name,
                    "Quantity": item.quantity,
                    "Unit Price": item.unit_price,
                    "Subtotal": item.subtotal,
                    "Total Sale": sale.total_amount,
                })
        df = pd.DataFrame(data)
        return self.export_as_csv(df, "sales.csv")

    @action(detail=False, methods=['post'])
    def import_sales_csv(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)
        df = pd.read_csv(file)
        for _, row in df.iterrows():
            Sale.objects.update_or_create(
                invoice_number=row['Invoice #'],
                defaults={
                    'date': row['Date'],
                    'total_amount': row['Total Sale'],
                }
            )
        return Response({"status": "Sales imported successfully."})

    @action(detail=False, methods=['get'])
    def export_purchases_csv(self, request):
        purchases = self.get_date_filtered_queryset(Purchase, request)
        data = []
        for purchase in purchases.select_related('supplier').prefetch_related('purchasetransactions'):
            for item in purchase.purchasetransactions.all():
                data.append({
                    "Invoice #": purchase.invoice_number,
                    "Date": purchase.purchase_date,
                    "Supplier": purchase.supplier.name if purchase.supplier else '',
                    "Product": item.product.name,
                    "Quantity": item.quantity,
                    "Unit Price": item.unit_price,
                    "Subtotal": item.subtotal,
                    "Total Purchase": purchase.total_amount,
                })
        df = pd.DataFrame(data)
        return self.export_as_csv(df, "purchases.csv")

    @action(detail=False, methods=['post'])
    def import_purchases_csv(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)
        df = pd.read_csv(file)
        for _, row in df.iterrows():
            Purchase.objects.update_or_create(
                invoice_number=row['Invoice #'],
                defaults={
                    'purchase_date': row['Date'],
                    'total_amount': row['Total Purchase'],
                }
            )
        return Response({"status": "Purchases imported successfully."})
