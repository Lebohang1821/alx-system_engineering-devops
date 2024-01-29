#!/usr/bin/python3
'''It exports data in the CSV format.'''
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Fetching todo data from JSONPlaceholder API
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()

    # Fetching user data from JSONPlaceholder API
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()

    user = [i for i in users if i.get('id') == int(argv[1])][0]

    # Filtering tasks based on the provided user ID
    tasks = [i for i in data if i.get('userId') == int(argv[1])]

    # Writing data to a CSV file
    with open(argv[1] + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

        # Writing header row
        writer.writerow(['User ID', 'Username', 'Completed', 'Title'])

        # Writing data for each task
        for task in tasks:
            writer.writerow([str(argv[1]), user.get('username'),
                             str(task.get('completed')), task.get('title')])

        # Closing the file
        f.close()
