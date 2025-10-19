#!/usr/bin/python3
"""Export data to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos"
                         "?userId={}".format(user_id)).json()

    username = user.get("username")

    task_list = []
    for todo in todos:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        task_list.append(task_dict)

    data = {user_id: task_list}

    filename = "{}.json".format(user_id)
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
