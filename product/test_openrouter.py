import requests

API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "meta-llama/llama-3.3-70b-instruct:free",
    "messages": [
        {
            "role": "user",
            "content": "Diga olá para mim."
        }
    ]
}

response = requests.post(BASE_URL, headers=headers, json=data)

print("Status code:", response.status_code)
try:
    print("Resposta JSON:", response.json())
except Exception as e:
    print("Erro ao decodificar JSON:", e)
    print("Texto bruto:", response.text)
