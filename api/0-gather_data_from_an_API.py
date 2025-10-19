#!/usr/bin/python3
"""
Script that retrieves and displays employee TODO list progress from an API
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get("name")
    
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
