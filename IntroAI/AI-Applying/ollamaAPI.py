import requests

url = 'http://localhost:11434/api/chat'

# Dados da requisição
data = {
    "model": "llama3.2",
    "messages": [
        {"role": "system", "content": "Você é um assistente prestativo."},
        {
            "role": "user",
            "content": "Escreva um haiku sobre recursão em programação."
        }
    ],
    "stream": False
}

# Enviar a requisição
response = requests.post(url, json=data)

print(response.json()["message"]["content"])
