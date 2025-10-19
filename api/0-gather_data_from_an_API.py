#!/usr/bin/python3
"""
Script that retrieves and displays employee TODO list progress from an API
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)

    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    employee_name = user_data.get("name")
    completed_tasks = [task for task in todos_data if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos_data)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
