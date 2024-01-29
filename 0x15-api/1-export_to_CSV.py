#!/usr/bin/python3
'''It exports data in the CSV format.'''
import csv
import requests
from sys import argv


if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = [i for i in users if i.get('id') == int(argv[1])][0]
    tasks = [i for i in data if i.get('userId') == int(argv[1])]
    with open(argv[1] + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for task in tasks:
            writer.writerow([str(argv[1]), user.get('username'),
                             str(task.get('completed')), task.get('title')])
        f.close()
