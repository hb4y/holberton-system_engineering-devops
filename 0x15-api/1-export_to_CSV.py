#!/usr/bin/python3
"""
comsume API from https://jsonplaceholder.typicode.com
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        api = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]

        data = requests.get("{}/users/{}".format(api, user_id)).json()
        todos = requests.get("{}/users/{}/todos".format(api, user_id)).json()
        done = 0
        total = len(todos)
        tasks = []
        file_name = "{}.csv".format(user_id)

        with open(file_name, mode='w') as employee_file:
            writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
            name = data.get("name")

            for task in todos:
                writer.writerow([
                        user_id,
                        name,
                        task.get("completed"),
                        task.get("title")])
