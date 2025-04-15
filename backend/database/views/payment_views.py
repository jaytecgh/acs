from rest_framework import viewsets, filters
from database.models import Payment
from database.serializers import PaymentSerializer
from database.permissions import IsAdmin, IsAccount
from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from rest_framework.decorators import action


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['transaction_type']
    ordering_fields = ['amount_paid', 'payment_date']
    ordering = ['-payment_date']
    permission_classes = [IsAdmin | IsAccount]

    @action(detail=True, methods=['get'])
    def receipt(self, request, pk=None):
        payment = self.get_object()
        template = get_template('receipts/receipt.html')

        html = template.render({
            'payment': payment,
            'invoice_number': payment.get_invoice_number(),
            'due_balance': payment.get_due_balance()
        })

        pdf_file = HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=receipt_{payment.get_invoice_number()}.pdf'
        return response

    
