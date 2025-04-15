from rest_framework import viewsets, filters
from database.models import Sale
from database.serializers import SaleSerializer
from database.permissions import IsAdmin, IsOperations, IsSales
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from rest_framework.decorators import action

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
        template = get_template('invoices/sales_invoice.html')
        html = template.render({
            'sale': sale,
            'vat': round(sale.total_amount * 0.04, 2),
            'total_with_vat': round(sale.total_amount * 1.04, 2),
            })

        pdf_file = HTML(string=html).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={sale.invoice_number}.pdf'
        return response