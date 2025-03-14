import openfoodfacts
import requests
from product.IA_services import analisar_restricoes_alimentares
from product.models import Produto, Ingrediente, RestricaoAlimentar

# """Busca informações do produto pelo código de barras usando Open Food Facts."""

def get_product_by_barcode(barcode):
    try:
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            product_info = data.get("product", {})

            if product_info:
                return {
                    "codigo_de_barras": barcode,
                    "nome": product_info.get("product_name", "Nome não disponível"),
                    "ingredientes": product_info.get("ingredients_text", "Sem ingredientes informados"),
                    "lista_ingredientes": [i.get("text", "Desconhecido") for i in product_info.get("ingredients", [])],
                    "marca": product_info.get("brands", "Marca desconhecida"),
                    "categoria": product_info.get("categories", "Sem categoria"),
                    "quantidade": product_info.get("quantity", "Quantidade não informada"),
                    "paises_venda": product_info.get("countries", "Países não informados"),
                    "nutriscore": product_info.get("nutriscore_grade", "Sem Nutri-Score"),
                    "nova_group": product_info.get("nova_group", "Sem pontuação Nova"),
                    "alergenicos": product_info.get("allergens", "Nenhum alérgeno informado"),
                    "aditivos": product_info.get("additives_tags", []),
                    "embalagem": product_info.get("packaging", "Sem informações de embalagem"),
                    "tabela_nutricional": product_info.get("nutriments", {}),
                    "imagem": product_info.get("image_url", "Sem imagem"),
                }

        print(f" Produto {barcode} não encontrado.")
        return None

    except Exception as e:
        print(f" Erro ao buscar produto: {e}")
        return None

# """Salva um produto no banco de dados com análise de restrições alimentares"""
def salvar_produto_no_banco(product_data):
    if "codigo_de_barras" not in product_data:
        print(" Erro: código de barras não encontrado no product_data")
        return None

    produto, created = Produto.objects.get_or_create(
        codigo_de_barras=product_data["codigo_de_barras"],
        defaults={
            "nome": product_data.get("nome", "Desconhecido"),
            "marca": product_data.get("marca", "Marca desconhecida"),
            "imagem": product_data.get("imagem", None)
        }
    )

    # Criar ingredientes no banco
    lista_ingredientes = product_data.get("lista_ingredientes", [])
    ingredientes_objs = []
    for nome_ingrediente in lista_ingredientes:
        ingrediente, _ = Ingrediente.objects.get_or_create(nome=nome_ingrediente)
        ingredientes_objs.append(ingrediente)

    produto.ingredientes.set(ingredientes_objs)

    # Analisar restrições com IA
    restricoes_detectadas = analisar_restricoes_alimentares(lista_ingredientes)

    # Criar/vincular restrições ao produto
    for restricao_nome in restricoes_detectadas:
        restricao, _ = RestricaoAlimentar.objects.get_or_create(nome=restricao_nome)
        produto.restricoes.add(restricao)

    produto.save()
    return produto


# testes

if __name__ == "__main__":
    ingredientes = ["Leite", "Farinha de trigo", "Soja"]
    restricoes = analisar_restricoes_alimentares(ingredientes)
    print("Restrições detectadas:", restricoes)
