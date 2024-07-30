#!/usr/bin/python3
"""Exports data in the JSON format"""

import json
import requests


def get_users():
    """Fetches information about all users."""
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()


def get_todos():
    """Fetches all TODO items."""
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    return response.json()


def prepare_all_user_data():
    """Prepares the TODO list data for all users in JSON format."""
    users = get_users()
    todos = get_todos()

    all_user_data = {}
    for user in users:
        task_list = []
        for task in todos:
            if task["userId"] == user["id"]:
                task_list.append({
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"],
                })
        all_user_data[user["id"]] = task_list

    return all_user_data


def export_all_to_json():
    """Exports data for all users' TODO lists to a single JSON file."""
    data = prepare_all_user_data()
    filename = "todo_all_employees.json"
    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile, indent=4)  # Add indentation for readability
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    export_all_to_json()
