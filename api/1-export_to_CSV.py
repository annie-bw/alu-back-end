#!/usr/bin/python3
"""Export data to CSV"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos"
                         "?userId={}".format(user_id)).json()

    username = user.get("username")

    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                           todo.get("title")])
