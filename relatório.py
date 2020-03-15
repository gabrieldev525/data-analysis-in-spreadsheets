import csv

from utils import match_people

# utils functions
def header(title):
    print('=' * len(title))
    print(title)
    print('=' * len(title))

# importação e leitura dos dados
alunos_list = list()
dengue_list = list()
onibus_list = list()

with open('Base de Alunos2.csv', 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 0:
            continue

        alunos_list.append(row[0].split(';'))

with open('Base de Dengue2.csv', 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 0:
            continue

        dengue_list.append(row[0].split(';'))

with open('Base de Onibus2.csv', 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 0:
            continue

        onibus_list.append(row[0].split(';'))


# Ánalise e tratamento dos dados


"""
    Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO
    que frequentaram a escola, menos os cidadãos que tiveram dengue
"""
student_without_dengue = []  # 247, 262
for aluno in alunos_list:
    match = match_people(aluno, dengue_list)
    if not match:
        student_without_dengue.append(aluno)
