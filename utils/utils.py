from datetime import datetime
import json
from operator import itemgetter


def get_count_of_vacancy(filename):
    """
    Вернуть количество вакансий от текущего сервиса.
    Получать количество необходимо динамически из файла.
    """

    sj_count = 0
    hh_count = 0
    with open(filename, 'r', encoding='UTF-8') as file:
        vacancies_list = json.load(file)
        for item in vacancies_list:
            if item['source'] == "SuperJob":
                sj_count += 1
            if item['source'] == "HeadHunter":
                hh_count += 1
    print(f'На сайте SuperJob было найдено {sj_count} вакансий по вашему запросу. \n'
          f'На сайте HeadHunter было найдено {hh_count} вакансий по вашему запросу. \n')


def sorted_to_salary(filename):
    """
    Сортировка по ЗП динамически из файла
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        sort_to_salary = sorted(data, key=itemgetter('salary_to'), reverse=True)
    return sort_to_salary


def date_format(data):
    """
    Перевод даты в нужный формат
    """
    for i in data:
        if i["source"] == "HeadHunter":
            i['date'] = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S+%f').strftime('%d.%m.%Y')
        elif i["source"] == "SuperJob":
            i['date'] = datetime.utcfromtimestamp(i['date']).strftime('%d.%m.%Y')
    return data


def data_sorted(data):
    """
    Сортировка по дате
    """

    sort_to_data = sorted(data, key=itemgetter('date'), reverse=True)
    return sort_to_data
