#!/usr/bin/python3
"""Exports employee TODO list data to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": user_id}).json()

    username = user.get("username")

    filename = "{}.csv".format(user_id)
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
