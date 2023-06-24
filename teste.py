import requests

def buscar_solucoes(consulta):
    api_url = "https://api.stackexchange.com/2.3/search"
    params = {
        "order": "desc",
        "sort": "relevance",
        "intitle": consulta,
        "site": "stackoverflow",
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data

consulta = input("Digite o erro ou linha de código: ")
resultados = buscar_solucoes(consulta)

# Filtrar resultados pelo título desejado
titulo_desejado = consulta.lower()  # Converter para minúsculas para comparação
resultados_filtrados = [item for item in resultados["items"] if titulo_desejado in item["title"].lower()]

# Limitar o número de soluções exibidas
num_solucoes_exibidas = 5
resultados_limitados = resultados_filtrados[:num_solucoes_exibidas]

# Verificar se há resultados válidos na resposta
if len(resultados_limitados) > 0:
    mensagem = "Aqui estão as 5 soluções mais relevantes:\n"
    for i, item in enumerate(resultados_limitados, start=1):
        titulo = item["title"]
        link_resposta = item["link"]
        mensagem += f"{i}. {titulo}\n   {link_resposta}\n"
    print(mensagem)
else:
    print("Nenhuma solução encontrada.")
