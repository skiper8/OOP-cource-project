import json
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """

    def check_file(self, filename):
        if os.path.isfile(filename):
            pass
        else:
            with open(filename, 'w') as f:
                pass

    def insert_SJ(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        vacant_sj = []
        with open('vacantes.json', "w", encoding='UTF-8') as file:
            for i in range(len(data)):
                vacant_sj.append(
                    {
                        "source": 'SuperJob',
                        "name": data[i]['profession'],
                        "description": data[i]['candidat'],
                        "url": data[i]['link'],
                        "city": data[i]['town']['title'],
                        "employer": data[i]['firm_name'],
                        "salary_from": int(data[i]["payment_from"]),
                        "salary_to": int(data[i]["payment_to"]),
                    }
                )
            json.dump(vacant_sj, file, indent=4, ensure_ascii=False)
            return vacant_sj

    def insert_HH(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open('vacantes.json', "r", encoding='UTF-8') as file:
            vacant_hh = json.load(file)
        with open('vacantes.json', "w", encoding='UTF-8') as file:
            for i in range(len(data)):
                vacant_hh.append(
                    {
                        "source": 'HeadHunter',
                        "name": data[i]['name'],
                        "description": data[i]['snippet']['responsibility'],
                        "url": data[i]['alternate_url'],
                        "city": data[i]["area"]["name"],
                        "employer": data[i]['employer']['name'],
                        "salary_from": data[i]["salary"]["from"],
                        "salary_to": data[i]["salary"]["to"],
                    }
                )
            json.dump(vacant_hh, file, indent=4, ensure_ascii=False)
            return vacant_hh

    def select(self, query, filename):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        results = []
        with open(filename, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            for i in data:
                if all(i.get(key) == value for key, value in query.items()):
                    results.append(i)
        return results

    def delete(self, query, filename):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """

        if not query:  # если передан пустой словарь
            print("Пустой запрос, удаление невозможно.")
            return

        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        new_data = [record for record in data if not all(x in record.items() for x in query.items())]

        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)
