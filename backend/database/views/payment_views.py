from rest_framework import viewsets, filters
from database.models import Payment
from database.serializers import PaymentSerializer
from database.permissions import IsAdmin, IsAccount
from django.template.loader import get_template
from django.http import HttpResponse
from rest_framework.decorators import action
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from decimal import Decimal

 

# --- PaymentViewSet ---
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin | IsAccount]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['transaction_type']
    ordering_fields = ['amount_paid', 'payment_date']
    ordering = ['-payment_date']

    @action(detail=True, methods=['get'])
    def receipt(self, request, pk=None):
        payment = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=receipt_{payment.id}.pdf'

        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, "Payment Receipt")
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 100, f"Invoice No: {payment.invoice_number}")
        p.drawString(50, height - 120, f"Amount Paid: GHS {payment.amount_paid:.2f}")
        p.drawString(50, height - 140, f"Date: {payment.payment_date.strftime('%Y-%m-%d')}")
        p.drawString(50, height - 180, "Received By: ______________________")

        p.showPage()
        p.save()
        return response