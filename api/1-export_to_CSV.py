#!/usr/bin/python3
"""
Script that exports employee TODO list data to CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)

    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    username = user_data.get("username")

    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])
