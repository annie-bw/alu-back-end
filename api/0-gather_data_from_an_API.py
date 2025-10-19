#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Fetch user's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos = requests.get(todos_url).json()

    # Count completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{len(todos)}):")

    for task in completed_tasks:
        print(f"\t {task}")
