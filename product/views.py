from rest_framework import viewsets
from .models import Produto, Ingrediente, RestricaoAlimentar, HistoricoConsulta
from .serializers import (
    ProdutoSerializer, IngredienteSerializer,
    RestricaoAlimentarSerializer, HistoricoConsultaSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

