from rest_framework import viewsets, filters
from database.models import Sale
from database.serializers import SaleSerializer
from database.permissions import IsAdmin, IsOperations, IsSales
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from rest_framework.decorators import action
from decimal import Decimal

# --- SaleViewSet ---
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['client__name', 'invoice_number', 'status']
    ordering_fields = ['sales_date', 'total_amount']
    ordering = ['-sales_date']
    permission_classes = [IsAdmin | IsOperations | IsSales]

    @action(detail=True, methods=['get'])
    def invoice(self, request, pk=None):
        sale = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={sale.invoice_number}.pdf'

        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        vat = round(sale.total_amount * 0.04, 2)
        total_with_vat = round(sale.total_amount * 1.04, 2)

        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, f"Sales Invoice #{sale.invoice_number}")
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 100, f"Client: {sale.client.name}")
        p.drawString(50, height - 120, f"Date: {sale.sales_date.strftime('%Y-%m-%d')}")
        p.drawString(50, height - 160, f"Amount: GHS {sale.total_amount:.2f}")
        p.drawString(50, height - 180, f"VAT (4%): GHS {vat:.2f}")
        p.drawString(50, height - 200, f"Total (incl. VAT): GHS {total_with_vat:.2f}")
        p.drawString(50, height - 260, "Authorized Signature: ______________________")
        p.showPage()
        p.save()
        return response