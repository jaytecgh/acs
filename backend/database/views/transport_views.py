from rest_framework import viewsets, filters
from rest_framework.decorators import action
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from decimal import Decimal

from database.models import Transport
from database.serializers import TransportSerializer
from database.permissions import IsAdmin, IsOperations

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsAdmin | IsOperations]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['transaction_type', 'vehicle_number']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    @action(detail=True, methods=['get'])
    def receipt(self, request, pk=None):
        transport = self.get_object()

        invoice_number = "-"
        items = []
        
        if transport.sale:
            invoice_number = transport.sale.invoice_number
            items = transport.sale.saletransactions.all()
        elif transport.purchase:
            invoice_number = transport.purchase.invoice_number
            items = transport.purchase.purchasetransactions.all()
            
        template = get_template('transport/transport_receipt.html')
        html = template.render({
            'transport': transport,
            'invoice_number': invoice_number,
            'items': items,
        })

        pdf_file = HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=transport_{transport.id}.pdf'
        return response
