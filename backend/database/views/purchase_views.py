from rest_framework import viewsets, filters
from database.models import Purchase
from database.serializers import PurchaseSerializer
from database.permissions import IsAdmin, IsOperations
from django.template.loader import get_template
from django.http import HttpResponse
from rest_framework.decorators import action
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from decimal import Decimal

    

# --- PurchaseViewSet ---
class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdmin | IsOperations]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['supplier__name', 'status']
    ordering_fields = ['purchase_date', 'total_amount']
    ordering = ['-purchase_date']

    @action(detail=True, methods=['get'])
    def invoice(self, request, pk=None):
        purchase = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={purchase.invoice_number}.pdf'

        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, f"Purchase Invoice #{purchase.invoice_number}")
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 100, f"Supplier: {purchase.supplier.name}")
        p.drawString(50, height - 120, f"Date: {purchase.purchase_date.strftime('%Y-%m-%d')}")
        p.drawString(50, height - 160, f"Amount: GHS {purchase.total_amount:.2f}")
        p.drawString(50, height - 220, "Authorized Signature: ______________________")

        p.showPage()
        p.save()
        return response
