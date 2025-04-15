from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Roles
ROLES = [
    ("admin", "Admin"),
    ("sales", "Sales"),
    ("account", "Account"),
    ("operations", "Operations"),
]

# ✅ Custom Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# ✅ Custom User Model
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# ✅ Employee Model
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employee")
    full_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.png')
    role = models.CharField(max_length=20, choices=ROLES, null=True, blank=True)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} ({self.role or 'Pending'})"


# Admin Table
class Admin(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk or not Admin.objects.filter(pk=self.pk, password=self.password).exists():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

# Suppliers Table
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    tin = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

#Category Table
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

#Unit Table
class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Product Table
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True)
    size = models.PositiveIntegerField(help_text="Size like 1, 5, 20, etc.")
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_stock_quantity(self):
        purchases = PurchaseTransaction.objects.filter(product=self).aggregate(total=models.Sum('quantity'))['total'] or 0
        sales = SaleTransaction.objects.filter(product=self).aggregate(total=models.Sum('quantity'))['total'] or 0
        return purchases - sales

    def save(self, *args, **kwargs):
        self.stock_quantity = self.get_stock_quantity()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.size} {self.unit})"


# Clients Table
class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Purchases Table
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateField()
    invoice_number = models.CharField(max_length=15, unique=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transportation_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

# Purchase Transactions Table
class PurchaseTransaction(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        InventoryLog.log_transaction(self.product, "Purchase", self.quantity)

# Sales Table
class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    sales_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    invoice_number = models.CharField(max_length=15, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            last_invoice = Sale.objects.order_by('-id').first()
            last_number = int(last_invoice.invoice_number.split('-')[-1]) + 1 if last_invoice and last_invoice.invoice_number else 1
            self.invoice_number = f"INV-{str(last_number).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number

# Sale Transactions Table
class SaleTransaction(models.Model):
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        InventoryLog.log_transaction(self.product, "Sale", -self.quantity)

# Payments Table
class Payment(models.Model):
    TRANSACTION_TYPE = [('Sales', 'Sales'), ('Purchase', 'Purchase')]
    STATUS_CHOICES = [('Unpaid', 'Unpaid'), ('Part Paid', 'Part Paid'), ('Paid', 'Paid')]
    PAYMENT_MODE_CHOICES = [('bank_transfer', 'Bank Transfer'), ('cheque', 'Cheque'), ('momo', 'MOMO'), ('cash', 'Cash')]

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE, null=True, blank=True)
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE, null=True, blank=True)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    withholding_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, default='cash')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unpaid')

    def __str__(self):
        return f"{self.transaction_type} Payment on {self.payment_date} - {self.status}"
    
    def get_invoice_number(self):
        if self.transaction_type == 'Sales' and self.sale:
            return self.sale.invoice_number
        elif self.transaction_type == 'Purchase' and self.purchase:
            return self.purchase.invoice_number
        return "-"

    def get_due_balance(self):
        base = 0
        if self.transaction_type == 'Sales' and self.sale:
            base = self.sale.total_amount
        elif self.transaction_type == 'Purchase' and self.purchase:
            base = self.purchase.total_amount
        return base - (self.amount_paid + self.withholding_tax)
    


# Inventory Log Table
class InventoryLog(models.Model):
    CHANGE_TYPE = [('Purchase', 'Purchase'), ('Sale', 'Sale')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=10, choices=CHANGE_TYPE)
    quantity_changed = models.IntegerField()
    log_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def log_transaction(product, change_type, quantity):
        InventoryLog.objects.create(product=product, change_type=change_type, quantity_changed=quantity)

# Transport Table
class Transport(models.Model):
    TRANSACTION_TYPE = [('Purchase', 'Purchase'), ('Sales', 'Sales')]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    driver_name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    from_location = models.TextField()
    to_location = models.TextField()
    transport_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_status = models.CharField(max_length=10, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)


# Reports Table
class Report(models.Model):
    REPORT_TYPE = [('Sales', 'Sales'), ('Purchases', 'Purchases'), ('Inventory', 'Inventory'), ('Profit', 'Profit'), ('Client Analysis', 'Client Analysis'), ('Expenditure', 'Expenditure')]
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE)
    report_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

# Expense Table
class Expense(models.Model):
    expense_type = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()