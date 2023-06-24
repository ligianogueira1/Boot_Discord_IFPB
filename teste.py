import requests
import xml.etree.ElementTree as ET

def pesquisar_artigos_arxiv(palavras_chave, max_resultados=5):
    base_url = 'http://export.arxiv.org/api/query'
    parametros = {
        'search_query': palavras_chave,
        'max_results': max_resultados,
        'sortBy': 'relevance',
        'sortOrder': 'descending',
    }

    response = requests.get(base_url, params=parametros)

    if response.status_code == 200:
        resultados = []

        # Parse do XML retornado pela API
        root = ET.fromstring(response.content)

        # Percorrer os elementos 'entry' no XML
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            # Extrair as informações dos artigos
            titulo = entry.find('{http://www.w3.org/2005/Atom}title').text
            autores = [autor.text for autor in entry.findall('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name')]
            pdf_url = entry.find('{http://www.w3.org/2005/Atom}link[@title="pdf"]').attrib['href']
            
            resultado = {
                'titulo': titulo,
                'autores': autores,
                'pdf_url': pdf_url,
            }
            resultados.append(resultado)

        return resultados
    else:
        # Tratar erros de requisição
        print('Ocorreu um erro na requisição:', response.status_code)
        return []

resultados = pesquisar_artigos_arxiv("machine learning")

for resultado in resultados:
    print(f'Título: {resultado["titulo"]}')
    print(f'Autores: {", ".join(resultado["autores"])}')
    print(f'Link de download: {resultado["pdf_url"]}')
    print()