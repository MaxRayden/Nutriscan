from openai import OpenAI

from product.vision_api import extract_text_from_image


def analisar_restricoes_alimentares(lista_ingredientes):
    prompt=f"""
    Identifique restrições alimentares com base nos seguintes ingredientes: {', '.join(lista_ingredientes)}.
    Responda apenas com os nomes das restrições conhecidas, como "Contém Leite - Intolerância à Lactose e Alergicos" ou "Contém Gluten - Alergia ao Glúten".
    """


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        extra_body={},
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(completion.choices[0].message.content)



def analisar_texto(extracted_text):
    prompt2=f""""
    O seguinte texto {', ' .join(extracted_text)}, que foi retirado de uma foto de um produto alimentício, 
    analise o texto e identifique:nome, ingredientes, 
    lista_ingredientes, marca, categoria, quantidade, paises_venda, 
    nutriscore, nova_group, alergenicos, aditivo, embalagem, tabela_nutricional, link_de_imagem
    e por fim faça uma análise e identifique as restrições alimentares e alergias e retorne um json"""

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        extra_body={},
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt2
            }
        ]
    )
    print(completion.choices[0].message.content)

# def __name__ == '__main__':
#     extract_text_= [""]












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

