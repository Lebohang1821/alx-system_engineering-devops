#!/usr/bin/python3
'''Returns information about TODO list progress by employee id and creates a CSV file.'''

import csv
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    # Fetch TODO list data from the API
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_data = todo_data.json()

    # Fetch user data from the API
    users_data = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_data.json()

    # Extract the user information based on the provided employee ID
    user = [i for i in users_data if i.get('id') == employee_id][0]

    # Filter tasks based on the provided employee ID
    tasks = [i for i in todo_data if i.get('userId') == employee_id]

    # Write data to CSV file
    csv_filename = f"{employee_id}_todo_progress.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["User ID", "Username", "Completed", "Title"])
        for task in tasks:
            writer.writerow([str(employee_id), user.get('username'),
                             str(task.get('completed')), task.get('title')])

    print(f"CSV file '{csv_filename}' created successfully.")


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
