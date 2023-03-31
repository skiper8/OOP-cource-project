from abc import ABC, abstractmethod
import os
import requests


class Engine(ABC):
    word = input("Введите ключевое слово для поиска - ")

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):

    def get_request(self):
        """
        Парсим данные с ресурса HeadHunter
        """

        my_auth_data = {'X-Api-App-Id': os.environ['HH_API_KEY']}
        url = 'https://api.hh.ru/vacancies?text=' + self.word
        vacancies_list_hh = []
        for item in range(50):
            request_hh = requests.get(url, headers=my_auth_data,
                                      params={"keywords": self.word, 'page': item}).json()['items']
            for item2 in request_hh:
                if item2["salary"] is None:
                    item2["salary"] = {}
                    item2["salary"]["from"] = 0
                    item2["salary"]["to"] = 0
                if item2["salary"]["from"] is None:
                    item2["salary"]["from"] = 0
                if item2["salary"]["to"] is None:
                    item2["salary"]["to"] = 0
                if item2["salary"]["from"] > item2["salary"]["to"]:
                    tmp = item2["salary"]["from"]
                    item2["salary"]["from"] = item2["salary"]["to"]
                    item2["salary"]["to"] = tmp
                vacancies_list_hh.append(item2)
        return vacancies_list_hh


class SuperJob(Engine):
    """
    Парсим данные с ресурса SuperJob
    """

    def get_request(self):
        my_auth_data = {'X-Api-App-Id': os.environ['SJ_API_KEY']}
        url = 'https://api.superjob.ru/2.0/vacancies/'
        vacancies_list_sj = []
        for item in range(50):
            request_sj = requests.get(url, headers=my_auth_data,
                                      params={"keywords": self.word, 'page': item}).json()['objects']
            for item2 in request_sj:
                if item2['payment_from'] is None:
                    item2['payment_from'] = 0
                if item2['payment_to'] is None:
                    item2['payment_to'] = 0
                if item2['payment_from'] > item2['payment_to']:
                    tmp = item2['payment_from']
                    item2['payment_from'] = item2['payment_to']
                    item2['payment_to'] = tmp
                vacancies_list_sj.append(item2)
        return vacancies_list_sj
