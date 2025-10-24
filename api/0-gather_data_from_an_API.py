#!/usr/bin/python3
"""
This module retrieves todos for a given user from the JSONPlaceholder API
and displays the completed tasks along with the total number of tasks.
"""

import requests
import sys


def fetch_todos():
    """Fetch all todos from the API and return as a list of dictionaries."""
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code != 200:
        print("Failed to fetch todos")
        sys.exit(1)
    return response.json()


def fetch_user(user_id):
    """Fetch user info by user_id and return the user's name."""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    if response.status_code != 200:
        print("Failed to fetch user information")
        sys.exit(1)
    return response.json().get("name", "Unknown")


def display_tasks(user_name, todos, user_id):
    """
    Display completed tasks for the given user.

    Args:
        user_name (str): Name of the user
        todos (list): List of todo dictionaries
        user_id (int): ID of the user
    """
    total_tasks = 0
    completed_tasks_

