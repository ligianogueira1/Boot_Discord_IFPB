import arxiv
import pandas as pd
import smtplib
import random
import email.message
import requests
from config import password, email_bot


students = pd.read_csv('data/alunos.csv')
teachers = pd.read_csv('data/professores.csv')

def authenticate(user):
    """Receives the email entered by a user and checks if it is present in a database.

    The function verifies if the email provided by the user is present in the databases of students
    and teachers. If it is present, it returns the corresponding name and a boolean value True to indicate
    successful authentication. Otherwise, it returns None and a boolean value False.

    Args:
        user (str): The email entered by the user for authentication.

    Returns:
        tuple: A tuple containing the name associated with the authenticated email (if found) and a boolean value
        indicating if the authentication was successful.

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
    """Generates a random key composed of uppercase letters, lowercase letters, and digits.

    The function generates a random key with 6 characters, consisting of a combination of uppercase letters,
    lowercase letters, and digits. The generated key can be used for various purposes, such as generating
    temporary passwords, access tokens, unique identifiers, among others.

    Returns:
        str: A random key composed of 6 alphanumeric characters.

    Raises:
        None.

    """
    key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&%$#@', k=6))
    return key

def send_email(addressee, key):
    """
    Sends an email with the verification code to the specified recipient.

    Args:
        addressee (str): The email address of the recipient.
        key (str): The verification code to be included in the email.

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
    msg['Subject'] = "código de verificação do servidor"
    msg['From'] = f'{email_bot}'
    msg['To'] = f'{addressee}'
 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def pesquisar_artigos_arxiv(palavras_chave, max_resultados=5):
    resultados = arxiv.Search(query=palavras_chave, max_results=max_resultados).results()
    return resultados

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