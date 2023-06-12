import pandas as pd

students = pd.read_csv('data/alunos.csv')
teachers = pd.read_csv('data/professores.csv')

def authenticator(user):

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