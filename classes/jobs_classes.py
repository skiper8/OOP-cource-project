import json


class Vacancy:
    __slots__ = ('name', 'description', 'url', 'salary_to', 'salary_from', 'source', 'city', 'date')
    i = 0

    def __init__(self, name, description, url, salary_to, salary_from, source, city, date, *args, **kwargs):
        self.source = source
        self.name = name
        self.description = description
        self.city = city
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.date = date

    def __str__(self):
        return f'Вакансия из {self.source}. ' \
               f'{self.name}, вот ссылка {self.url}. \n' \
               f'Зарпалта от {self.salary_to} до {self.salary_from}. \n' \
               f'Дата размещения {self.date}\n'
