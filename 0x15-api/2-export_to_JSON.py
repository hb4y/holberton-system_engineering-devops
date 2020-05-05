#!/usr/bin/python3
"""
comsume API from https://jsonplaceholder.typicode.com
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        api = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]

        data = requests.get("{}/users/{}".format(api, user_id)).json()
        todos = requests.get("{}/users/{}/todos".format(api, user_id)).json()
        tasks = []
        file_name = "{}.json".format(user_id)

        for task in todos:
            aux = {}
            aux['task'] = task.get("title")
            aux['completed'] = task.get("completed")
            aux['username'] = data.get("username")
            tasks.append(aux)
        to_dict = {user_id: tasks}

        with open(file_name, mode='w') as employee_file:
            json.dump(to_dict, employee_file)
