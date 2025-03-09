from huggingface_hub import InferenceClient


def analisar_restricoes_alimentares(lista_ingredientes):

    prompt=f"""
    Identifique restrições alimentares com base nos seguintes ingredientes: {', '.join(lista_ingredientes)}.
    Responda apenas com os nomes das restrições conhecidas, como "Contém Leite - Intolerância à Lactose e Alergicos" ou "Contém Gluten - Alergia ao Glúten".
    """

    client = InferenceClient(
        provider="fireworks-ai",
        api_key="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"
    )

    messages = [

        {
            "role": "user",
            "content": prompt
        }
    ]

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct",
        messages=messages,
        max_tokens=500,
    )

    print(completion.choices[0].message)
    return completion.choices[0].message.content.split(", ")
