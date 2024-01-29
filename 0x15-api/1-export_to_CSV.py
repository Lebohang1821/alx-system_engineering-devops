#!/usr/bin/python3
'''It exports data in the CSV format.'''
import csv
import requests
from sys import argv

# Fetch todo data from the JSONPlaceholder API
data = requests.get('https://jsonplaceholder.typicode.com/todos')
data = data.json()

# Fetch user data from the JSONPlaceholder API
users = requests.get('https://jsonplaceholder.typicode.com/users')
users = users.json()

# Find the user based on the provided user ID
user = [i for i in users if i.get('id') == int(argv[1])][0]

# Filter tasks based on the provided user ID
tasks = [i for i in data if i.get('userId') == int(argv[1])]

# Create a CSV file with the provided user ID as the filename
with open(argv[1] + '.csv', 'w', newline='') as f:
    # Create a CSV writer with quoting set to QUOTE_NONNUMERIC
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    # Write headers to the CSV file
    writer.writerow(['UserID', 'Username', 'Completed', 'Title'])

    # Write each task's information to the CSV file
    for task in tasks:
        writer.writerow([str(argv[1]), user.get('username'),
                         str(task.get('completed')), task.get('title')])
    # Close the file
    f.close()
