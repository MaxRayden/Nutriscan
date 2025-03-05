from google.cloud import vision
import io
import openfoodfacts
import requests



# """Extrai texto de uma imagem usando Google Vision API."""

def extract_text_from_image(image_path):

    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    texts = response.text_annotations
    if texts:
        return texts[0].description  # Retorna o texto principal detectado

    return None


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


