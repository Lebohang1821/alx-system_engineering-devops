#!/usr/bin/python3
'''It returns information about his/her TODO list progress'''
import requests
from sys import argv

if __name__ == '__main__':
    # Fetch TODO list data from the API
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_data = todo_data.json()

    # Fetch user data from the API
    users_data = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_data.json()

    # Extract the user information based on the provided employee ID
    user = [i for i in users_data if i.get('id') == int(argv[1])][0]

    # Filter tasks based on the provided employee ID
    tasks = [i for i in todo_data if i.get('userId') == int(argv[1])]

    # Filter completed tasks
    completed_tasks = [i for i in tasks if i.get('completed') is True]

    # Display the TODO list progress information
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed_tasks), len(tasks)))

    # Display the titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
