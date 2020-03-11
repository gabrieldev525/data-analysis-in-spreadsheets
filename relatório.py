import csv

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
peoples_with_dengue = list(map(lambda x : x[1], dengue_list))
alunos_without_dengue = list(filter(lambda x : x[1] not in peoples_with_dengue, alunos_list))

header('Alunos que não tiveram dengue')
print('\n{:^6}    {:>8}    {:>39}\n'.format('ID', 'NOME', 'DATA DE NASCIMENTO'))
for aluno in alunos_without_dengue:
    print(f'{aluno[0]:^6}   {aluno[1]:>30}    {aluno[5]:>10}')

# Teste dos dados fornecidos
alunos_without_dengue_test = list(map(lambda x : x[1], alunos_without_dengue))
count = 0
for i in alunos_without_dengue_test:
    if i in peoples_with_dengue:
        count += 1

print('\n')
header('Teste dos dados fornecidos')
print(f'\nforam encontrados {count} alunos na lista que tiveram dengue')
print(f'Inicialmente a lista de alunos possuia {len(alunos_list)} registros e depois do filtro passou a ter {len(alunos_without_dengue)}')
