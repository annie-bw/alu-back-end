#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    completed_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed_tasks), total_tasks
        )
    )

    for title in completed_tasks:
        print("\t {}".format(title))
