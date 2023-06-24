import email.message
import random
import requests
import smtplib
import xml.etree.ElementTree as ET
from database import *
from config import *

def authenticate(user):
    """Recebe o e-mail inserido pelo usuário e verifica se está presente em um banco de dados.

    A função verifica se o e-mail fornecido pelo usuário está presente nos bancos de dados dos alunos
    e dos professores. Se estiver presente, retorna o nome correspondente e um valor booleano True para indicar
    autenticação bem-sucedida. Caso contrário, retorna None e um valor booleano False.

    Args:
        user (str): O e-mail inserido pelo usuário para autenticação.

    Returns:
        tuple: Uma tupla contendo o nome associado ao e-mail autenticado (se encontrado) e um valor booleano
        indicando se a autenticação foi bem-sucedida.

    Raises:
        None.
    """

    if user in students['E-mail academico'].values:
        filter_name = students.loc[students['E-mail academico'] == user, 'Nome'].values
        name = filter_name.item()
        return name, True

    elif user in teachers['E-mail'].values:
        filter_name = teachers.loc[teachers['E-mail'] == user, 'Nome'].values
        name = filter_name.item()
        return name, True

    else:
        return None, False

def random_key():
    """Gera uma chave aleatória composta por letras maiúsculas, letras minúsculas e dígitos.

    A função gera uma chave aleatória com 6 caracteres, composta por uma combinação de letras maiúsculas,
    letras minúsculas e dígitos. A chave gerada pode ser usada para diversos fins, como gerar senhas temporárias,
    tokens de acesso, identificadores únicos, entre outros.

    Returns:
        str: Uma chave aleatória composta por 6 caracteres alfanuméricos.

    Raises:
        None.
    """
    key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&%$#@', k=6))
    return key

def send_email(addressee, key):
    """
    Envia um e-mail com o código de verificação para o destinatário especificado.

    Args:
        addressee (str): O endereço de e-mail do destinatário.
        key (str): O código de verificação a ser incluído no e-mail.

    Returns:
        None

    Raises:
        None
    """

    corpo_email = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
            body {{
                font-family: 'Roboto', sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 6px;
                box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                font-size: 24px;
                margin-bottom: 20px;
                color: #333333;
            }}
            p {{
                font-size: 18px;
                margin-bottom: 10px;
                color: #555555;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Você resolveu entrar para o lado certo da força! Aqui está o seu código:</h1>
            <p>{key}</p>
        </div>
    </body>
    </html>
    """

    msg = email.message.Message()
    msg['Subject'] = "Código de verificação do servidor"
    msg['From'] = f'{email_bot}'
    msg['To'] = f'{addressee}'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def pesquisar_artigos_arxiv(palavras_chave, max_resultados=5):
    """
    Pesquisa artigos no arXiv com base nas palavras-chave fornecidas.

    Args:
        palavras_chave (str): Palavras-chave para a pesquisa.
        max_resultados (int, opcional): Número máximo de resultados a serem retornados.
            O valor padrão é 5.

    Returns:
        list: Uma lista de dicionários contendo os resultados da pesquisa, com as seguintes chaves:
            - "titulo" (str): Título do artigo.
            - "autores" (list): Lista de autores do artigo.
            - "pdf_url" (str): URL de download do artigo em formato PDF.

    Example:
        resultados = pesquisar_artigos_arxiv('aprendizado de máquina', max_resultados=10)
        for resultado in resultados:
        print(resultado['titulo'])
    """
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
            titulo = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', '')
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


def buscar_solucoes(consulta):
    """
    Pesquisa soluções no Stack Overflow com base na consulta fornecida.

    Args:
        consulta (str): A consulta ou mensagem de erro a ser pesquisada.

    Returns:
        dict: Um dicionário contendo a resposta JSON da API do Stack Overflow.

    Example:
        resultados = buscar_solucoes('compreensão de lista em python')
        for item in resultados['items']:
            print(item['title'])
    """
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