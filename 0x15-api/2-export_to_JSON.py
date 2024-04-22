#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, user_id)
    username = requests.get(user_endpoint).json().get("username")
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in tasks
            if task.get("userId") == user_id
        ]
    }

    # Serialize data in json file
    with open("{}.json".format(user_id), 'w', encoding="utf-8") as f:
        json.dump(user_tasks, f)
