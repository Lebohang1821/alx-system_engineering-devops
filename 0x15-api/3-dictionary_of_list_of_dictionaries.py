#!/usr/bin/python3
'''It extends Python script to export data in JSON format'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    with open('todo_all_employees.json', 'w', newline='') as f:
        res = {}
        for user in users:
            user_id = str(user.get('id'))
            tasks = [i for i in data if i.get('userId') == int(user_id)]
            expo = {user_id: []}
            task_list = expo.get(user_id)
            for task in tasks:
                task_list.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')
                })
            res.update(expo.copy())
            expo.clear()
        f.write(json.dumps(res))
