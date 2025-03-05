from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Produto, Ingrediente, RestricaoAlimentar, HistoricoConsulta
from .serializers import (
    ProdutoSerializer, IngredienteSerializer,
    RestricaoAlimentarSerializer, HistoricoConsultaSerializer
)
from .vision_api import extract_text_from_image, get_product_by_barcode
import os
import tempfile
import requests



class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RestricaoAlimentarViewSet(viewsets.ModelViewSet):
    queryset = RestricaoAlimentar.objects.all()
    serializer_class = RestricaoAlimentarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HistoricoConsultaViewSet(viewsets.ModelViewSet):
    queryset = HistoricoConsulta.objects.all()
    serializer_class = HistoricoConsultaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# """API para extrair texto de uma imagem"""

class OCRView(APIView):

    def post(self, request):
        if "image" not in request.FILES:
            return Response({"error": "Nenhuma imagem enviada"}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES["image"]

        # Criar um arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
            for chunk in image.chunks():
                temp_image.write(chunk)
            temp_image_path = temp_image.name  # Caminho do arquivo temporário

        try:
            extracted_text = extract_text_from_image(temp_image_path)
        finally:
            os.remove(temp_image_path)  # Remover a imagem após o processamento

        return Response({"texto_extraido": extracted_text}, status=status.HTTP_200_OK)

# """API para buscar produto pelo código de barras"""

class ProductByBarcodeView(APIView):

    def get(self, request, barcode):
        product_info = get_product_by_barcode(barcode)

        if product_info:
            return Response(product_info, status=status.HTTP_200_OK)

        return Response({"error": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)