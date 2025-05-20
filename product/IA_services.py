import json
from product.IA_client import client
from product.vision_api import extract_text_from_image


def limpar_resposta_markdown(texto):
    """Remove blocos de código markdown da resposta da IA."""
    if texto.startswith("```json") or texto.startswith("```"):
        return "\n".join([
            line for line in texto.splitlines()
            if not line.strip().startswith("```")
        ]).strip()
    return texto


def analisar_restricoes_alimentares(lista_ingredientes):
    prompt = f"""
Você é um assistente que analisa ingredientes de produtos alimentícios. 

Dada a lista de ingredientes: {', '.join(lista_ingredientes)}, responda apenas com um JSON contendo uma chave "restricoes" que seja uma lista com as restrições alimentares encontradas.

Exemplo de resposta JSON:
{{
  "restricoes": [
    "Contém Leite - Intolerância à Lactose e Alergicos",
    "Contém Glúten - Alergia ao Glúten"
  ]
}}

Não inclua texto fora do JSON.
"""

    try:
        response = client.chat_completion(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[{"role": "user", "content": prompt}]
        )
        resposta_texto = response["choices"][0]["message"]["content"].strip()
        resposta_texto = limpar_resposta_markdown(resposta_texto)
        resposta_json = json.loads(resposta_texto)
        return resposta_json.get("restricoes", [])

    except Exception as e:
        print("Erro ao decodificar JSON da resposta:", e)
        print("Resposta bruta da IA:", resposta_texto)
        return []


def analisar_texto(extracted_text):
    prompt = f"""
O seguinte texto {', '.join(extracted_text)}, que foi retirado de uma foto de um produto alimentício, 
analise o texto e identifique os seguintes campos:
- nome
- ingredientes
- lista_ingredientes
- marca
- categoria
- quantidade
- paises_venda
- nutriscore
- nova_group
- alergenicos
- aditivo
- embalagem
- tabela_nutricional
- link_de_imagem

E por fim, faça uma análise das restrições alimentares e alergias. 
Retorne um JSON contendo todos esses campos. Apenas o JSON, sem explicações adicionais.
"""

    try:
        response = client.chat_completion(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[{"role": "user", "content": prompt}]
        )
        resposta_texto = response["choices"][0]["message"]["content"].strip()
        resposta_texto = limpar_resposta_markdown(resposta_texto)
        return json.loads(resposta_texto)

    except Exception as e:
        print("Erro ao decodificar JSON da resposta:", e)
        print("Resposta bruta da IA:", resposta_texto)
        return {}


# Teste rápido
if __name__ == "__main__":
    ingredientes = ["Leite", "Farinha de trigo", "Soja"]
    restricoes = analisar_restricoes_alimentares(ingredientes)
    print("Restrições detectadas:", restricoes)

    # Exemplo opcional de uso com imagem
    # texto_extraido = extract_text_from_image("caminho/para/imagem.jpg")
    # resultado = analisar_texto(texto_extraido)
    # print(json.dumps(resultado, indent=2, ensure_ascii=False))


    #
    # prompt=f"""
    # Identifique restrições alimentares com base nos seguintes ingredientes: {', '.join(lista_ingredientes)}.
    # Responda apenas com os nomes das restrições conhecidas, como "Contém Leite - Intolerância à Lactose e Alergicos" ou "Contém Gluten - Alergia ao Glúten".
    # """
    #
    # client = InferenceClient(
    #     provider="fireworks-ai",
    #     # api_key="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"
    #     api_key = "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"
    # )
    #
    # messages = [
    #
    #     {
    #         "role": "user",
    #         "content": prompt
    #     }
    # ]
    #
    # completion = client.chat.completions.create(
    #     model="meta-llama/Llama-3.3-70B-Instruct",
    #     messages=messages,
    #     max_tokens=500,
    # )
    #
    # print(completion.choices[0].message)
    # return completion.choices[0].message.content.split(", ")

