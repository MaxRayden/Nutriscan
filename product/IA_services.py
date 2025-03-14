from openai import OpenAI



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

