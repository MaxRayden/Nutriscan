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
from .vision_api import extract_text_from_image
from .services import get_product_by_barcode, salvar_produto_no_banco
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

# """Buscar produto pelo código de barras"""
class ProductByBarcodeView(APIView):

    def get(self, request, barcode):

        produto = Produto.objects.filter(codigo_de_barras=barcode).first()

        if produto:
            return Response({"message": "Produto encontrado no banco", "produto": ProdutoSerializer(produto).data}, status=status.HTTP_200_OK)

        product_info = get_product_by_barcode(barcode)

        if not product_info:
            return Response({"error": "Produto não encontrado na API"}, status=status.HTTP_404_NOT_FOUND)

        produto = salvar_produto_no_banco(product_info)

        if not produto:
            return Response({"error": "Erro ao salvar produto no banco"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(ProdutoSerializer(produto).data, status=status.HTTP_200_OK)
