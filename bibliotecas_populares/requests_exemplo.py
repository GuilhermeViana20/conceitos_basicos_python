import requests

resposta = requests.get("https://api.github.com")
print("Status:", resposta.status_code)
print("Dados:", resposta.json())