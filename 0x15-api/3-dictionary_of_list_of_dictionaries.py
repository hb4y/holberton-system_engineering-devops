#!/usr/bin/python3
"""
comsume API from https://jsonplaceholder.typicode.com
"""
import json
import requests
import sys


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(api)).json()
    todos = requests.get("{}/todos".format(api)).json()
    file_name = "todo_all_employees.json"
    to_dict = {}

    for user in users:
        tasks = []
        for task in todos:
            aux = {}
            aux['task'] = task.get("title")
            aux['completed'] = task.get("completed")
            aux['username'] = user.get("username")
            tasks.append(aux)
        to_dict[user.get('id')] = tasks

    with open(file_name, mode='w') as employee_file:
        json.dump(to_dict, employee_file)
