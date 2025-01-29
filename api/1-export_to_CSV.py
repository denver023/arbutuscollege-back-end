#!/usr/bin/python3
"""
Script that exports TODO list information for a given employee ID to CSV format
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports TODO list information for a specific employee to CSV format
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

        # Write to CSV file
        filename = "{}.csv".format(employee_id)
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([
                    employee_id,
                    user.get('username'),
                    task.get('completed'),
                    task.get('title')
                ])
    except requests.RequestException:
        return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        export_to_csv(int(sys.argv[1]))
