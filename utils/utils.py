import os
import json

import requests as requests

sj_api_key: str = os.getenv('SJ_API_KEY')
my_auth_data = {'X-Api-App-Id': os.environ['SJ_API_KEY']}

response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=my_auth_data, params={"keywords": 'word'})

print(response)
