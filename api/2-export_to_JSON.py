#!/usr/bin/python3
"""
Script that exports employee TODO list data to JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    username = user.get("username")

    tasks_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    json_data = {employee_id: tasks_list}

    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)
