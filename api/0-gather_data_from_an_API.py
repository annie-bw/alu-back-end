#!/usr/bin/python3
"""
Script that retrieves and displays employee TODO list progress from an API
"""
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

    completed = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task.get("title")))
