#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    # Get user info
    user_data = requests.get(user_url).json()
    if not user_data or 'name' not in user_data:
        print("Employee ID not found")
        sys.exit(1)

    user_name = user_data['name']

    # Get todos
    todos = requests.get(todo_url).json()

    # Count tasks
    total_tasks = len(todos)
    completed_tasks = [t['title'] for t in todos if t['completed']]

    # Print results
    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
