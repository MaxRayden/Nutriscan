from rest_framework import serializers
from .models import Produto, Ingrediente, RestricaoAlimentar, HistoricoConsulta

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nome', 'descricao']

class RestricaoAlimentarSerializer(serializers.ModelSerializer):
    ingredientes_perigosos = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = RestricaoAlimentar
        fields = ['id', 'nome', 'descricao', 'ingredientes_perigosos']

class ProdutoSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    restricoes = RestricaoAlimentarSerializer(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'marca', 'codigo_de_barras', 'ingredientes', 'restricoes', 'imagem', 'criado_em', 'atualizado_em']

class HistoricoConsultaSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = HistoricoConsulta
        fields = ['id', 'usuario', 'produto', 'data_consulta']
