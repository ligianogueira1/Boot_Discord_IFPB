import pandas as pd
import smtplib
import random
from config import smtp_username, smtp_password

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
    key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=8))
    return key

def send_email(destinatario, key):
    """Sends an email containing an authentication key to the specified recipient.

    The function uses an SMTP server to send an email to the recipient containing the provided authentication key.
    The SMTP server and authentication credentials should be properly configured before using this function.

    Args:
        destinatario (str): The email address of the recipient.
        key (str): The authentication key to be sent.

    Returns:
        None

    Raises:
        smtplib.SMTPException: Exception raised in case of failure to send the email.

    """

    smtp_server = 'seu_servidor_smtp'
    smtp_port = 587
    

    subject = 'Chave de autenticação'
    message = f'Aqui está a sua chave de autenticação: {key}'
    email_message = f'Subject: {subject}\n\n{message}'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, destinatario, email_message)
