#!/usr/bin/python3
"""Gather data from an API"""
import csv
from urllib.request import urlopen
import json
from sys import argv

userId = argv[1]

url = f'https://jsonplaceholder.typicode.com/users?id={userId}'
with urlopen(url) as res:
    body = res.read().decode('UTF-8')
data = json.loads(body)
username = data[0]['username']

url = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
with urlopen(url) as res:
    body = res.read().decode('UTF-8')

data = json.loads(body)
with open(f'{userId}.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for task in data:
        writer.writerow(
            [f'"{task["userId"]}"',
             f'"{username}"',
             f'"{task["completed"]}"',
             f'"{task["title"]}"']
        )
