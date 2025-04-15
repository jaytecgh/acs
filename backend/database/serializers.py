from rest_framework import serializers
from django.contrib.auth import get_user_model
from database.models import (
    Employee, Admin, Supplier, Product, Client, Purchase, PurchaseTransaction, 
    Sale, SaleTransaction, Payment, InventoryLog, Transport, Expense, 
    Report, Unit, Category
)

User = get_user_model()

# ✅ User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'is_staff']

# ✅ Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            'id', 'user', 'full_name', 'role',
            'can_edit', 'can_delete', 'profile_image', 'profile_image_url'
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        return super().update(instance, validated_data)

    def get_profile_image_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None

# Admin Serializer with password hashing
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

# Unit Serializer
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Purchase Transaction Serializer
class PurchaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseTransaction
        fields = '__all__'

# Purchase Serializer
class PurchaseSerializer(serializers.ModelSerializer):
    purchasetransactions = PurchaseTransactionSerializer(many=True, read_only=True, source='purchasetransaction_set')

    class Meta:
        model = Purchase
        fields = '__all__'


# Sales Transaction Serializer
class SaleTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleTransaction
        fields = '__all__'

# Sale Serializer
class SaleSerializer(serializers.ModelSerializer):
    saletransactions = SaleTransactionSerializer(many=True, read_only=True, source='saletransaction_set')

    class Meta:
        model = Sale
        fields = '__all__'

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['status']

    def validate(self, data):
        amount = data.get('amount_paid', 0)
        withholding = data.get('withholding_tax', 0)
        transaction_type = data.get('transaction_type')

        # Get expected total
        if transaction_type == 'Sales' and data.get('sale'):
            total = data['sale'].total_amount
        elif transaction_type == 'Purchase' and data.get('purchase'):
            total = data['purchase'].total_amount
        else:
            total = 0

        # Combine actual payment + withheld tax
        net_paid = amount + withholding

        if net_paid >= total:
            data['status'] = 'Paid'
        elif net_paid > 0:
            data['status'] = 'Part Paid'
        else:
            data['status'] = 'Unpaid'

        return data


# Inventory Log Serializer
class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = '__all__'

# Transport Serializer
class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'

# Expense Serializer
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

# Report Serializer
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
