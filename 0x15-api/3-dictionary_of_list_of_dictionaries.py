#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()

    dict_to_write = {
            user.get("id"): [{
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")}
                for todo in requests.
                get("{}todos".format(url),
                    params={'userId': user.get("id")}).json()]
            for user in users
            }
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dict_to_write, json_file)
