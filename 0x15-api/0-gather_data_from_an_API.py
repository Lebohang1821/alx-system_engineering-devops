#!/usr/bin/python3
'''It returns information about his/her TODO list progress'''
import requests
from sys import argv

if __name__ == '__main__':
    # Fetching todo data from JSONPlaceholder API
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()

    # Fetching user data from JSONPlaceholder API
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()

    # Extracting user information based on the provided user ID from command line argument
    user = [i for i in users if i.get('id') == int(argv[1])][0]

    # Filtering tasks based on the provided user ID
    tasks = [i for i in data if i.get('userId') == int(argv[1])]

    # Filtering completed tasks
    completed = [i for i in tasks if i.get('completed') is True]

    # Printing a summary of completed tasks for the specified user
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(tasks)))

    # Printing details of each completed task
    for task in completed:
        print("\t {}".format(task.get('title')))
