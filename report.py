# python imports
import csv

# third imports
import xlsxwriter

# local imports
from utils import match_people

workbook = xlsxwriter.Workbook('report.xlsx')

header_title = ['ID', 'Nome', 'Nome da Mae', 'Nome do Pai', 'Sexo', 'Data de Nascimento']

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
tab = workbook.add_worksheet('Questão 01')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Id')
row = 1
for student in student_list:
    match = match_people(student, dengue_list)
    if not match:
        student_without_dengue.append(student)
        tab.write(row, 0, student[1])
        tab.write(row, 1, student[5])
        tab.write(row, 2, student[0])
        row += 1

print(f'1) {len(student_without_dengue)}')

"""
    2) Relatório Saúde: Informar nome, data de nascimento e data que tiveram dengue dos
    cidadãos de XPTO que frequentaram o posto de saúde, menos os cidadãos que não
    utilizam ônibus.
"""
tab = workbook.add_worksheet('Questão 02')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Data que tiveram dengue')
peoples_with_dengue_without_no_bus = []
row = 1
for people in dengue_list:
    match = match_people(people, bus_list)
    if match:
        peoples_with_dengue_without_no_bus.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[6])
        row += 1
print(f'2) {len(peoples_with_dengue_without_no_bus)}')

"""
    3) Relatório Mobilidade: Informar nome, data de nascimento e linhas de ônibus dos cidadãos
    de XPTO que utilizaram o transporte público e não tiveram dengue.
"""
tab = workbook.add_worksheet('Questão 03')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Linhas de ônibus')
peoples_use_bus_without_dengue = []
row = 1
for people in bus_list:
    match = match_people(people, dengue_list)
    if not match:
        peoples_use_bus_without_dengue.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[6])
        row += 1
print(f'3) {len(peoples_use_bus_without_dengue)}')

"""
    4) Relatório Educação e Saúde: Informar nome, data de nascimento, id e data que tiveram
    dengue dos cidadãos de XPTO que frequentaram a escola e tiveram dengue.
"""
tab = workbook.add_worksheet('Questão 04')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'ID')
tab.write(0, 3, 'Data que teve dengue')
students_with_dengue = []
row = 1
for people in student_list:
    match = match_people(people, dengue_list)
    if match:
        students_with_dengue.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[0])
        tab.write(row, 3, match[6])
        row += 1
print(f'4) {len(students_with_dengue)}')

"""
    5) Relatório Educação e Mobilidade: Informar nome, data de nascimento, id e linhas de ônibus
    dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público.
"""
tab = workbook.add_worksheet('Questão 05')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'ID')
tab.write(0, 3, 'Linhas de ônibus')
students_that_use_bus = []
row = 1
for student in student_list:
    match = match_people(student, bus_list)
    if match:
        students_that_use_bus.append([*student, match[6]])
        tab.write(row, 0, student[1])
        tab.write(row, 1, student[5])
        tab.write(row, 2, student[0])
        tab.write(row, 3, match[6])
        row += 1
print(f'5) {len(students_that_use_bus)}')

"""
    6) Relatório Saúde e Mobilidade: Informar nome, data de nascimento, data que tiveram dengue e
    linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público.
"""
tab = workbook.add_worksheet('Questão 06')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Data que teve dengue')
tab.write(0, 3, 'Linhas de ônibus')
peoples_use_bus_with_dengue = []
row = 1
for people in dengue_list:
    match = match_people(people, bus_list)
    if match:
        peoples_use_bus_with_dengue.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[6])
        tab.write(row, 3, match[6])
        row += 1
print(f'6) {len(peoples_use_bus_with_dengue)}')

"""
    7) Relatório Saúde, Mobilidade e Educação: Informar nome, data de nascimento, data que tiveram dengue e linhas
    de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde, utilizaram transporte público e frequentaram a escola.
"""
tab = workbook.add_worksheet('Questão 07')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Data que teve dengue')
tab.write(0, 3, 'Linhas de ônibus')
students_with_dengue_and_use_bus = []
row = 1
for student in students_that_use_bus:
    match = match_people(student, dengue_list)
    if match:
        students_with_dengue_and_use_bus.append(student)
        tab.write(row, 0, student[1])
        tab.write(row, 1, student[5])
        tab.write(row, 2, student[6])
        tab.write(row, 3, student[7])
        row += 1
print(f'7) {len(students_with_dengue_and_use_bus)}')

"""
    8) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    mas não utilizaram transporte público.
"""
tab = workbook.add_worksheet('Questão 08')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Data que teve dengue')
peoples_with_dengue_no_use_bus = []
row = 1
for people in dengue_list:
    match = match_people(people, bus_list)
    if not match:
        peoples_with_dengue_no_use_bus.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[6])
        row += 1
print(f'8) {len(peoples_with_dengue_no_use_bus)}')

"""
    9) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    mas não frequentaram a escola.
"""
tab = workbook.add_worksheet('Questão 09')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Data que teve dengue')
peoples_with_dengue_no_school = []
row = 1
for people in dengue_list:
    match = match_people(people, student_list)
    if not match:
        peoples_with_dengue_no_school.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[6])
        row += 1
print(f'9) {len(peoples_with_dengue_no_school)}')

"""
    10) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    mas não frequentaram a escola, nem utilizaram transporte público.
"""
tab = workbook.add_worksheet('Questão 10')
tab.write(0, 0, 'Nome')
tab.write(0, 1, 'Data de nascimento')
tab.write(0, 2, 'Data que teve dengue')
people_with_dengue_no_school_and_no_use_bus = []
row = 1
for people in dengue_list:
    if people in peoples_with_dengue_no_use_bus and \
       people in peoples_with_dengue_no_school:
        people_with_dengue_no_school_and_no_use_bus.append(people)
        tab.write(row, 0, people[1])
        tab.write(row, 1, people[5])
        tab.write(row, 2, people[6])
        row += 1
print(f'10) {len(people_with_dengue_no_school_and_no_use_bus)}')


# [RESULT MANUAL EXCEL, RESULT FINAL SCRIPT]
results = [
    [255, len(student_without_dengue)],
    [5, len(peoples_with_dengue_without_no_bus)],
    [233, len(peoples_use_bus_without_dengue)],
    [11, len(students_with_dengue)],
    [13, len(students_that_use_bus)],
    [7, len(peoples_use_bus_with_dengue)],
    [31, len(students_with_dengue_and_use_bus)],
    [233, len(peoples_with_dengue_no_use_bus)],
    [229, len(peoples_with_dengue_no_school)],
    [191, len(people_with_dengue_no_school_and_no_use_bus)]
]

tab = workbook.add_worksheet('RESULTADOS FINAIS')
tab.write(0, 0, 'Questão')
tab.write(0, 1, 'Resultado feito pelo o excel')
tab.write(0, 2, 'Resultado script')

for row, result in enumerate(results):
    tab.write(row + 1, 0, row + 1)
    for column, value in enumerate(result):
        tab.write(row + 1, column + 1, value)
workbook.close()
