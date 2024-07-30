#!/usr/bin/python3
"""
This script utilizes json to return information about employeet 
"""

import requests
from sys import argv

def get_user_info(user_id):
  """Fetches user information based on the given ID."""
  response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
  return response.json()

def get_todos():
  """Fetches all TODO items."""
  return requests.get("https://jsonplaceholder.typicode.com/todos").json()

def calculate_progress(user_id):
  """Calculates the progress of a user's TODO list."""
  user_data = get_user_info(user_id)
  todos = get_todos()

  completed_tasks = sum(1 for task in todos if task['userId'] == user_id and task['completed'])
  total_tasks = sum(1 for task in todos if task['userId'] == user_id)

  return user_data['name'], completed_tasks, total_tasks

def main():
  user_id = argv[1]
  name, completed, total = calculate_progress(user_id)
  print(f"Employee {name} is done with tasks ({completed}/{total}):")
  print('\n'.join(f"\t {task['title']}" for task in get_todos() if task['userId'] == int(user_id) and task['completed']))

if __name__ == "__main__":
  main()

