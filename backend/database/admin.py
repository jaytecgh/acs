from django.contrib import admin
from .models import Employee
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'role', 'can_edit', 'can_delete']
    search_fields = ['user__email', 'full_name']
