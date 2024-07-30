#!/usr/bin/python3
"""Exports data in the JSON format"""


import json
import requests
from sys import argv


def get_user_info(user_id):
  """Fetches user information based on the given ID."""
  response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
  return response.json()


def get_todos():
  """Fetches all TODO items."""
  return requests.get("https://jsonplaceholder.typicode.com/todos").json()


def prepare_user_data(user_id):
  """Prepares the user's TODO list data in JSON format."""
  user_data = get_user_info(user_id)
  todos = get_todos()

  todo_list = []
  for task in todos:
    if task["userId"] == user_id:
      todo_list.append({
          "task": task["title"],
          "completed": task["completed"],
          "username": user_data["username"],
      })

  return {user_id: todo_list}


def export_to_json(user_id):
  """Exports user's TODO list data to a JSON file."""
  data = prepare_user_data(user_id)
  filename = f"{user_id}.json"
  with open(filename, mode="w") as jsonfile:
    json.dump(data, jsonfile, indent=4)  # Add indentation for readability
  print(f"Data exported to {filename}")


def main():
  user_id = argv[1]
  export_to_json(user_id)


if __name__ == "__main__":
  main()

