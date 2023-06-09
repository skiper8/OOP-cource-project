from classes.engine_classes import *
from classes.jobs_classes import *
from classes.connector import *
from utils.utils import *

# счетчик вакансий
count_vac = 0
# здесь будут храниться отсортированные данные
sort_file = []
# здесь будут храниться экземпряры класса Vacancy
vacancies = []
connector = Connector()
# проверяем на существование файл. Если его нет то создаем
connector.check_file('vacantes.json')
sj = SuperJob()
data_sj = sj.get_request()
hh = HH()
data_hh = hh.get_request()
connector.insert_SJ(data_sj)
connector.insert_HH(data_hh)
get_count_of_vacancy('vacantes.json')

print("Как хотите отсортировать? (ЗП \ Город \ Дата)")
user_input = input('')

if user_input.lower() == "зп":
    sort_file = sorted_to_salary('vacantes.json')
    sort_file = date_format(sort_file)
elif user_input.lower() == "город":
    print("Какой город вас интересует?")
    user_input = input('')
    sort_file = connector.select({'city': user_input}, 'vacantes.json')
    sort_file = date_format(sort_file)
elif user_input.lower() == "дата":
    with open('vacantes.json', 'r', encoding='UTF-8') as file:
        sort_file = json.load(file)
    sort_file = date_format(sort_file)
    sort_file = data_sorted(sort_file)

# Запись экземпляров класса Vacancy в список vacants
for i in sort_file:
    v = Vacancy(i['name'], i['description'], i['url'], i["salary_from"], i["salary_to"], i['source'], i['city'],
                i['date'])
    vacancies.append(v)
if len(vacancies) == 0:
    print("Извините, но по вашему запросу ничего не найдено")
    exit()
print("Вот 10 вакансий по вашему запросу.")

# Вывод вакансий пользователю
for i in vacancies:
    if i is vacancies[-1]:
        print(f'\n'
              f'На этом список подошел к концу.')
        exit()
    print(i)
    count_vac += 1
    if count_vac == 10:
        print("Показать следующие 10 вакансий? (Да \ Нет)")
        user_input = input("")
        if user_input.lower() == "да":
            count_vac = 0
            continue
        else:
            exit()
