#!/usr/bin/python3
"""Fetches and displays a user's TODO list progress from an API."""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": user_id}).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task))
