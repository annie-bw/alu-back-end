#!/usr/bin/python3
"""
Script to fetch an employee’s TODO list progress from an API.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    # Get user data
    user = requests.get(user_url).json()
    user_name = user.get("name")

    # Get todos data
    todos = requests.get(todos_url).json()

    # Compute totals
    total_tasks = len(todos)
    completed_tasks = [t.get("title") for t in todos if t.get("completed")]

    # Display progress
    print(f"Employee {user_name} is done with tasks"
          f"({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task}")
