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
    1) Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO
    que frequentaram a escola, menos os cidadãos que tiveram dengue
"""
student_without_dengue = []
for student in student_list:
    match = match_people(student, dengue_list)
    if not match:
        student_without_dengue.append(student)
print(f'1) {len(student_without_dengue)}')

"""
    2) Relatório Saúde: Informar nome, data de nascimento e data que tiveram dengue dos
    cidadãos de XPTO que frequentaram o posto de saúde, menos os cidadãos que não
    utilizam ônibus.
"""
peoples_with_dengue_without_no_bus = []
for people in dengue_list:
    match = match_people(people, bus_list)
    if match:
        peoples_with_dengue_without_no_bus.append(people)
print(f'2) {len(peoples_with_dengue_without_no_bus)}')

"""
    3) Relatório Mobilidade: Informar nome, data de nascimento e linhas de ônibus dos cidadãos
    de XPTO que utilizaram o transporte público e não tiveram dengue.
"""
peoples_use_bus_without_dengue = []
for people in bus_list:
    match = match_people(people, dengue_list)
    if not match:
        peoples_use_bus_without_dengue.append(people)
print(f'3) {len(peoples_use_bus_without_dengue)}')

"""
    4) Relatório Educação e Saúde: Informar nome, data de nascimento, id e data que tiveram
    dengue dos cidadãos de XPTO que frequentaram a escola e tiveram dengue.
"""
students_with_dengue = []
for student_from_all in student_list:
    if student_from_all not in student_without_dengue:
        students_with_dengue.append(student_from_all)
print(f'4) {len(students_with_dengue)}')

"""
    5) Relatório Educação e Mobilidade: Informar nome, data de nascimento, id e linhas de ônibus
    dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público.
"""
students_that_use_bus = []
for student in student_list:
    match = match_people(student, bus_list)
    if match:
        students_that_use_bus.append(student)
print(f'5) {len(students_that_use_bus)}')

"""
    6) Relatório Saúde e Mobilidade: Informar nome, data de nascimento, data que tiveram dengue e
    linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público.
"""
peoples_use_bus_with_dengue = []
for people in dengue_list:
    match = match_people(people, bus_list)
    if match:
        peoples_use_bus_with_dengue.append(people)
print(f'6) {len(peoples_use_bus_with_dengue)}')

"""
    7) Relatório Saúde, Mobilidade e Educação: Informar nome, data de nascimento, data que tiveram dengue e linhas
    de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde, utilizaram transporte público e frequentaram a escola.
"""
students_with_dengue_and_use_bus = []
for student in students_that_use_bus:
    match = match_people(student, dengue_list)
    if match:
        students_with_dengue_and_use_bus.append(student)
print(f'7) {len(students_with_dengue_and_use_bus)}')

"""
    8) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    mas não utilizaram transporte público.
"""
peoples_with_dengue_no_use_bus = []
for people in dengue_list:
    match = match_people(people, bus_list)
    if not match:
        peoples_with_dengue_no_use_bus.append(people)
print(f'8) {len(peoples_with_dengue_no_use_bus)}')

"""
    9) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    mas não frequentaram a escola.
"""
peoples_with_dengue_no_school = []
for people in dengue_list:
    match = match_people(people, student_list)
    if not match:
        peoples_with_dengue_no_school.append(people)
print(f'9) {len(peoples_with_dengue_no_school)}')

"""
    10) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    mas não frequentaram a escola, nem utilizaram transporte público.
"""
people_with_dengue_no_school_and_no_use_bus = []
for people in dengue_list:
    if people in peoples_with_dengue_no_use_bus and \
       people in peoples_with_dengue_no_school:
        people_with_dengue_no_school_and_no_use_bus.append(people)
print(f'10) {len(people_with_dengue_no_school_and_no_use_bus)}')
