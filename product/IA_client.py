import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")

print(API_KEY)
print(BASE_URL)

class OpenRouterClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer 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",
            "Content-Type": "application/json",
            "Referer": "http://localhost",
            "X-Title": "nutriScanBackend"
        }

    def chat_completion(self, model, messages):
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=self.headers,
            json={
                "model": model,
                "messages": messages
            }
        )
        response.raise_for_status()
        return response.json()

client = OpenRouterClient(API_KEY, BASE_URL)
