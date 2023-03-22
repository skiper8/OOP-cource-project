from abc import ABC, abstractmethod
import os
import requests
import json


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    word = 'Python'
    my_auth_data = {'X-Api-App-Id': os.environ['HH_API_KEY']}
    url = 'https://api.hh.ru/vacancies?text=' + word

    def get_request(self):
        vacancies_list_hh = []
        for item in range(1):
            request_hh = requests.get(self.url, headers=self.my_auth_data,
                                      params={"keywords": self.word, 'page': item}).json()['items']
            for item2 in request_hh:
                vacancies_list_hh.append(item2)
        return vacancies_list_hh

    def save_to_json(self, file_path, vacancies_list_hh):
        with open(file_path, "w", encoding='UTF-8') as file:
            channel_info_hh = []
            for i in range(len(vacancies_list_hh)):
                channel_info_hh.append(
                    {
                        "source": 'SuperHH',
                        "name": vacancies_list_hh[i]['name'],
                        "url": vacancies_list_hh[i]['url'],
                        "salary": vacancies_list_hh[i]['salary'],
                    }
                )
            json.dump(channel_info_hh, file, indent=4, ensure_ascii=False)


class SuperJob(Engine):
    word = 'Python'
    my_auth_data = {'X-Api-App-Id': os.environ['SJ_API_KEY']}
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_request(self):
        vacancies_list_sj = []
        for item in range(1):
            request_sj = requests.get(self.url, headers=self.my_auth_data,
                                      params={"keywords": self.word, 'page': item}).json()['objects']
            for item2 in request_sj:
                vacancies_list_sj.append(item2)
        return vacancies_list_sj

    def save_to_json(self, file_path, vacancies_list_sj):

        with open(file_path, "w", encoding='UTF-8') as file:
            channel_info_sj = []
            for i in range(len(vacancies_list_sj)):
                channel_info_sj.append(
                    {
                        "source": 'SuperJob',
                        "name": vacancies_list_sj[i]['profession'],
                        "url": vacancies_list_sj[i]['link'],
                        "salary": f'{vacancies_list_sj[i]["payment_to"]} - {vacancies_list_sj[i]["payment_from"]}',
                    }
                )
            json.dump(channel_info_sj, file, indent=4, ensure_ascii=False)


sj = SuperJob()
vacancies_list_sj = sj.get_request()
sj.save_to_json('../vacant_SJ.json', vacancies_list_sj)
hh = HH()
vacancies_list_hh = hh.get_request()
hh.save_to_json('../vacant_HH.json', vacancies_list_hh)
