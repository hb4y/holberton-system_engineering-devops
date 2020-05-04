#!/usr/bin/python3
"""
comsume API
"""
import sys
import requests


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user_data = requests.get("{}/users/{}".format(api, user_id)).json()
    user_todos = requests.get("{}/users/{}/todos".format(api, user_id)).json()
    done_task = 0
    total_task = len(user_todos)
    tasks = []

    for task in user_todos:
        if task["completed"] is True:
            done_task += 1
        tasks.append("\t " + task["title"])

    print("Employee {} is done with tasks({}/{}):".format(
            user_data["name"], done_task, total_task))
    print('\n'.join(tasks))
