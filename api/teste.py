#UMA API É UM JEITO DE CONECTAR SISTEMAS, INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTES SISTEMAS
#DE SOFTWARE SE COMUNIQUEM E TROQUEM DADOS ENTRE SÍ;

#NESTE EXEMPLO, SERÁ UTILIZADO A WEATHERapi.com PARA CONSULTAR AS CONDIÇÕES
#CLIMÁTICAS DE UMA DETERMINADA LOCALIDADE;

#CONSUMIR API ->
#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UMA CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÁ DEFINIDA

import string

import requests #Biblioteca para fazer requisições HTTP
from pprint import pprint #Biblioteca para imprimir os dados de forma legível


#VAMOS PRECISAR DA APIKEY -> UMA CREDENCIAL
API_Key = "" 

API_link = ""

parametros ={
    "key":API_Key,
    "q":"São Paulo",#Cidade para qual queremos obter os dados
    "lang":"pt" #linguagem
}
#armazenamento a resposta da requisição  na variável resposta
response = requests.get(API_link, parametros)
print(response)

if response.status_code == 200:
    data = response.json()
    location = data['location']['name']
    country = data['location']['country']
    temperature_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    print()
    print(40 * "=")
    print("Dados do clima obtidos com sucesso!")
    print(40 * "-")
    print(f"Localização: {location}, {country}")
    print(40 * "-")
    print(f"Temperatura: {temperature_c}°C")
    print(40 * "-")
    print(f"Condição: {condition}")
    print(40 * "=")

else:
    print("Erro ao obter dados da API:", response.status_code)