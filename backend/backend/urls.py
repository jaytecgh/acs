"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from database.views.auth_views import MyTokenObtainPairView
from database.views.user_management import UserViewSet, EmployeeViewSet
from database.views.dashboard import DashboardStatsView
from database.views import (
    auth_views,
    ProductViewSet, 
    AdminViewSet, 
    InventoryLogViewSet,
    SaleViewSet,
    PurchaseViewSet,
    ClientViewSet,
    SupplierViewSet,
    ExpenseViewSet,  
    ReportViewSet,
    TransportViewSet,
    PaymentViewSet,
    CategoryViewSet,
    UnitViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'units', UnitViewSet)
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'inventorylogs', InventoryLogViewSet)
router.register(r'transports', TransportViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'reports', ReportViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Construction Supply - API",
        default_version='v1',
        description="API documentation for the Construction Supply System",
        contact=openapi.Contact(email="j.tecgh@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # JWT Auth endpoints
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),  # optional logout
    
    # Registration still needed
    path('auth/register/', auth_views.register, name='register'),

    path('auth/forgot-password/', auth_views.forgot_password, name='forgot-password'),
    path('auth/reset-password/', auth_views.reset_password, name='reset-password'),

    path("dashboard/", DashboardStatsView.as_view(), name="dashboard-stats"),

    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# ✅ Add router.urls to the final urlpatterns
urlpatterns += router.urls
