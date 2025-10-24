#!/usr/bin/python3
"""
This module retrieves todos for a given user from the JSONPlaceholder API
and displays the completed tasks along with the total number of tasks.
"""

import requests
import sys


def main():
    """
    Main function to fetch and display a user's todos.

    Usage:
        python3 0-gather_data_from_an_API.py <user_id>
    
    Args:
        user_id (int): The ID of the user to retrieve todos for.
    """
    try:
        user_id = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: python3 0-gather_data_from_an_API.py <user_id>")
        sys.exit(1)

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    # Get todos and user information
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Failed to fetch todos")
        sys.exit(1)
    todos = response.json()

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to fetch user information")
        sys.exit(1)
    user_name = user_response.json().get('name', 'Unknown')

    # Filter todos for the specified user
    total_tasks = 0
    completed_tasks = []

    for todo in todos:
        if todo.get('userId') == user_id:
            total_tasks += 1
            if todo.get('completed'):
                completed_tasks.append(todo.get('title'))

    # Print results
    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    main()

