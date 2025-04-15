from rest_framework import viewsets, filters
from database.models import Purchase
from database.serializers import PurchaseSerializer
from database.permissions import IsAdmin, IsOperations
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from rest_framework.decorators import action
from decimal import Decimal


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['supplier__name', 'status']
    ordering_fields = ['purchase_date', 'total_amount']
    ordering = ['-purchase_date']
    permission_classes = [IsAdmin | IsOperations]


    @action(detail=True, methods=['get'])
    def invoice(self, request, pk=None):
        purchase = self.get_object()
        vat = round(purchase.total_amount * Decimal('0.01219'), 2)
        final_total = round(purchase.total_amount + vat + purchase.transportation_cost, 2)
        
        template = get_template('invoices/purchase_invoice.html')
        html = template.render({
            'purchase': purchase,
            'vat': vat,
            'final_total': final_total
        })

        pdf_file = HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={purchase.invoice_number}.pdf'
        return response


    
