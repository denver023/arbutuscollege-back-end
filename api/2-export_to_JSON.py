#!/usr/bin/python3
"""
Script that exports TODO list information for a given employee ID to JSON format
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports TODO list information for a specific employee to JSON format
    Args:
        employee_id: Integer ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Get employee information
        user_url = "{}/users/{}".format(base_url, employee_id)
        todo_url = "{}/todos".format(base_url)

        user = requests.get(user_url).json()
        todos = requests.get(todo_url, params={'userId': employee_id}).json()

        # Prepare JSON data
        tasks = []
        for task in todos:
            tasks.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')
            })

        json_data = {str(employee_id): tasks}

        # Write to JSON file
        filename = "{}.json".format(employee_id)
        with open(filename, 'w') as json_file:
            json.dump(json_data, json_file)

    except requests.RequestException:
        return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        export_to_json(int(sys.argv[1]))
