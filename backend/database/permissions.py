from rest_framework import permissions
from rest_framework.permissions import BasePermission

def get_user_role(request):
    return getattr(getattr(request.user, 'employee', None), 'role', None)

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_user_role(request) == 'admin'

class IsOperations(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_user_role(request) == 'operations'

class IsSales(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_user_role(request) == 'sales'

class IsAccount(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_user_role(request) == 'account'

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        role = get_user_role(request)
        if request.method in permissions.SAFE_METHODS:
            return True
        return role == 'admin'
