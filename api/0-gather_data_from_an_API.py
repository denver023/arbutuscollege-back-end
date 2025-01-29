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
    user_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos".format(base_url)

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todo_url, params={'userId': employee_id}).json()

        completed = [task for task in todos if task.get('completed')]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get('name'), len(completed), len(todos)))
        
        for task in completed:
            print("\t {}".format(task.get('title')))
    except requests.RequestException:
        return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee_todo_progress(int(sys.argv[1]))
