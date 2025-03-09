from django.test import TestCase

# testes de inferencia da llama
from huggingface_hub import InferenceClient



client = InferenceClient(
	provider="fireworks-ai",
	api_key="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"
)

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
	messages=messages,
	max_tokens=500,
)

print(completion.choices[0].message)