from django.contrib import admin
from django.urls import path, include
from product.views import OCRView, ProductByBarcodeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/products/', include('product.urls')),
    path('api/ocr/', OCRView.as_view(), name="ocr"),
    path('barcode/<str:barcode>/', ProductByBarcodeView.as_view(), name="barcode"),

]
