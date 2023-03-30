import os
import json
import csv

import requests as requests


filename = '../vacant_HH.json'

with open(filename, 'r') as file:
    o = json.loads(file.read())

name = o['name']
url = o['url']
salary_to = o['salary_to']
salary_from = o['salary_from']

