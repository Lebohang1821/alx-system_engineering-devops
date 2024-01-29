#!/usr/bin/python3
'''It extends my Python script to export data in the JSON format.'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = [i for i in users if i.get('id') == int(argv[1])][0]
    tasks = [i for i in data if i.get('userId') == int(argv[1])]

    with open(argv[1] + '.json', 'w', newline='') as f:
        expo = {argv[1]: []}
        task_list = expo.get(argv[1])
        for task in tasks:
            task_list.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')
            })
        f.write(json.dumps(expo))
