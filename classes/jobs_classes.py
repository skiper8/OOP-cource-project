import json
class Vacancy:
    __slots__ = ('name', 'description', 'url', 'salary_to', 'salary_from', 'source', 'city')
    i = 0

    def __init__(self, name, description, url, salary_to, salary_from, source, city, *args, **kwargs):
        self.source = source
        self.name = name
        self.description = description
        self.city = city
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from

    def __str__(self):
        return f'Вакансия из {self.source}. ' \
               f'{self.name}, вот ссылка {self.url}. ' \
               f'Зарпалта от {self.salary_to} до {self.salary_from}.'


class Count:

    @property
    def get_count_of_vacancy(self, filename):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(filename, 'r', encoding='UTF-8') as file:
            vacancies_list = json.loads(file.read())
            print(len(vacancies_list))


class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'SJ: {self.name}, зарплата от {self.salary_to} до {self.salary_from} руб/мес'


class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.name}, зарплата от {self.salary_to} до {self.salary_from} руб/мес'

    def sorting(vacancies):
        """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
        pass

    def get_top(vacancies, top_count):
        """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
        pass
