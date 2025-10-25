#!/usr/bin/python3
"""Script that returns information about a user's TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(user_url)
    user_name = user_response.json().get("name")

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = 0
    done_tasks = []

    for todo in todos:
        if todo.get("userId") == user_id:
            total_tasks += 1
            if todo.get("completed"):
                done_tasks.append(todo.get("title"))

   

