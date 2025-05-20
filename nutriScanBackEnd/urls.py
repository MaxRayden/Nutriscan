from django.contrib import admin
from django.urls import path, include
from product.views import OCRView, ProductByBarcodeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/products/', include('product.urls')),
    path('api/ocr/', OCRView.as_view(), name="ocr"),
    path('barcode/<str:barcode>/', ProductByBarcodeView.as_view(), name="barcode"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh

]
