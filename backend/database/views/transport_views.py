from rest_framework import viewsets, filters
from rest_framework.decorators import action
from django.template.loader import get_template
from django.http import HttpResponse
from decimal import Decimal
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from database.models import Transport
from database.serializers import TransportSerializer
from database.permissions import IsAdmin, IsOperations


# --- TransportViewSet ---
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
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=transport_{transport.id}.pdf'

        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, "Transport Receipt")
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 100, f"Transporter: {transport.transporter.name}")
        p.drawString(50, height - 120, f"Amount Paid: GHS {transport.amount:.2f}")
        p.drawString(50, height - 140, f"Date: {transport.date.strftime('%Y-%m-%d')}")
        p.drawString(50, height - 180, "Authorized By: ______________________")

        p.showPage()
        p.save()
        return response
