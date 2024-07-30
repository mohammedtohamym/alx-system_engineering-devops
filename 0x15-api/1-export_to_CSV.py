#!/usr/bin/python3
"""Exports data in the CSV format"""


import csv
import requests
from sys import argv


def get_user_info(user_id):
  """Fetches user information based on the given ID."""
  response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
  return response.json()


def get_todos():
  """Fetches all TODO items."""
  return requests.get("https://jsonplaceholder.typicode.com/todos").json()


def export_to_csv(user_id):
  """Exports user's TODO list data to a CSV file."""
  user_data = get_user_info(user_id)
  todos = get_todos()

  filename = f"{user_id}.csv"
  with open(filename, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(["user_id", "username", "completed", "title"])
    for task in todos:
      if task["userId"] == user_id:
        writer.writerow([user_id, user_data["username"], task["completed"], task["title"]])


def main():
  user_id = argv[1]
  export_to_csv(user_id)
  print(f"Data exported to {user_id}.csv")


if __name__ == "__main__":
  main()
