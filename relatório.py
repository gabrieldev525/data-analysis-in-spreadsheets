import csv

from utils import match_people


# utils functions
def header(title):
    print('=' * len(title))
    print(title)
    print('=' * len(title))


# importação e leitura dos dados
student_list = list()
dengue_list = list()
bus_list = list()

with open('Base de Alunos2.csv', 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 0:
            continue

        student_list.append(row[0].split(';'))

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

        bus_list.append(row[0].split(';'))


# Analysis and treatment of data

"""
    Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO
    que frequentaram a escola, menos os cidadãos que tiveram dengue
"""
student_without_dengue = []  # 247, 262
for student in student_list:
    match = match_people(student, dengue_list)
    if not match:
        student_without_dengue.append(student)

"""
    Relatório Saúde: Informar nome, data de nascimento e data que tiveram dengue dos
    cidadãos de XPTO que frequentaram o posto de saúde, menos os cidadãos que não
    utilizam ônibus.
"""
peoples_with_dengue_without_no_bus = []
for people in dengue_list:
    match = match_people(people, bus_list)
    if match:
        peoples_with_dengue_without_no_bus.append(people)

"""
    Relatório Mobilidade: Informar nome, data de nascimento e linhas de ônibus dos cidadãos
    de XPTO que utilizaram o transporte público e não tiveram dengue.
"""
peoples_use_bus_without_dengue = []
for people in bus_list:
    match = match_people(people, dengue_list)
    if not match:
        peoples_use_bus_without_dengue.append(people)

"""
    Relatório Educação e Saúde: Informar nome, data de nascimento, id e data que tiveram
    dengue dos cidadãos de XPTO que frequentaram a escola e tiveram dengue.
"""
students_with_dengue = []
for student_from_all in student_list:
    if student_from_all not in student_without_dengue:
        students_with_dengue.append(student_from_all)


"""
    Relatório Educação e Mobilidade: Informar nome, data de nascimento, id e linhas de ônibus
    dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público.
"""
students_that_use_bus = []
for student in student_list:
    match = match_people(student, bus_list)
    if match:
        students_that_use_bus.append(student)

"""
    Relatório Saúde e Mobilidade: Informar nome, data de nascimento, data que tiveram dengue e
    linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público.
"""
peoples_use_bus_with_dengue = []
for people in dengue_list:
    match = match_people(people, bus_list)
    if match:
        peoples_use_bus_with_dengue.append(people)

import ipdb; ipdb.set_trace()