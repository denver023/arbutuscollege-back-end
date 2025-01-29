#!/usr/bin/python3
"""
Script that retrieves TODO list progress for a given employee ID using REST API
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a specific employee
    Args:
        employee_id: Integer ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Get TODO list for employee
    todos_response = requests.get(f"{base_url}/todos",
                                params={'userId': employee_id})
    if todos_response.status_code != 200:
        return
    
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo.get('completed'))
    
    # Print progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    
    # Print completed task titles
    for todo in todos:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        sys.exit(1)
