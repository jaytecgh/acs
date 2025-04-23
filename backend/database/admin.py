from django.contrib import admin
from .models import Employee
from django.contrib.auth import get_user_model
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'role', 'can_edit', 'can_delete']
    search_fields = ['user__email', 'full_name']


User = get_user_model()
admin.site.register(User)
