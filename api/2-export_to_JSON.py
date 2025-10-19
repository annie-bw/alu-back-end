#!/usr/bin/python3
"""
Script that exports employee TODO list data to JSON format
"""
import json
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

    task_list = []
    for todo in todos_data:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        task_list.append(task_dict)

    export_data = {user_id: task_list}

    filename = "{}.json".format(user_id)
    with open(filename, 'w') as f:
        json.dump(export_data, f)
