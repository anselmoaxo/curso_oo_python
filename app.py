import requests
import json
import os

url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)


if response.status_code == 200:
    dados_json = response.json()
    # dicionario vazio 
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante]= []
        
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
         
else:
    print(f' Erro Numero: {response.status_code}')
    


pasta = 'data'
os.makedirs(pasta, exist_ok=True)


for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    with open(caminho_arquivo, 'w', encoding='utf-8') as nome_arq_restaurante:
        json.dump(dados, nome_arq_restaurante, indent=4, ensure_ascii=False)
        