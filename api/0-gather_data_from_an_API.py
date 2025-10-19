#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    # Fetch user info
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Fetch user's todos
    todos_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    )
    todos = requests.get(todos_url).json()

    # Completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed), len(todos)
        )
    )

    for task in completed:
        print("\t {}".format(task))
