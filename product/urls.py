from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProdutoViewSet, IngredienteViewSet, RestricaoAlimentarViewSet, HistoricoConsultaViewSet, OCRView, ProductByBarcodeView

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'restricoes', RestricaoAlimentarViewSet)
router.register(r'historico', HistoricoConsultaViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('ocr/', OCRView.as_view(), name="ocr"),
    path('barcode/<str:barcode>/', ProductByBarcodeView.as_view(), name="barcode"),

]

urlpatterns += router.urls
