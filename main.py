from classes.connector import *
from classes.engine_classes import *
from classes.jobs_classes import *

connector = Connector()
connector.check_file('vacantes.json')
sj = SuperJob()
data_sj = sj.get_request()
hh = HH()
data_hh = hh.get_request()
connector.insert_SJ(data_sj)
connector.insert_HH(data_hh)
vacantis = []
connector.delete({'salary_to': 0}, 'vacantes.json')
for i in connector.select({'city': 'Москва'}, 'vacantes.json'):
    v = Vacancy(i['name'], i['description'], i['url'], i["salary_from"], i["salary_to"], i['source'], i['city'])
    vacantis.append(v)

for i in vacantis:
    print(i)

