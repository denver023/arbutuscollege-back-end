#!/usr/bin/python3
"""
Script that exports TODO list information for all employees to JSON format
"""
import json
import requests


def export_all_tasks():
    """
    Exports all employees' TODO list information to JSON format
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)
    todos_url = "{}/todos".format(base_url)

    try:
        # Get all users
        users = requests.get(users_url).json()
        # Get all todos
        todos = requests.get(todos_url).json()

        # Create dictionary with user tasks
        all_tasks = {}
        for user in users:
            user_id = str(user.get('id'))
            user_tasks = []
            
            # Get tasks for current user
            for task in todos:
                if task.get('userId') == user.get('id'):
                    user_tasks.append({
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                    })
            
            all_tasks[user_id] = user_tasks

        # Write to JSON file
        with open('todo_all_employees.json', 'w') as json_file:
            json.dump(all_tasks, json_file)

    except requests.RequestException:
        return


if __name__ == "__main__":
    export_all_tasks()
