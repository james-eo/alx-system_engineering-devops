#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_endpoint = "{}/users".format(url)
    users = requests.get(user_endpoint).json()

    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()

    user_tasks = {
        user.get("id"): [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in tasks
            if task.get("userId") == user.get("id")
        ]
        for user in users
    }

    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        json.dump(user_tasks, f)
