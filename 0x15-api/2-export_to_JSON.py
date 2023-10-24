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
    user = requests.get("{}users".format(url),
                        params={'id': sys.argv[1]}).json()
    todos = requests.get("{}todos".format(url),
                         params={'userId': sys.argv[1]}).json()

    dict_to_write = {
            sys.argv[1]: [{
                "task": temp.get("title"),
                "completed": temp.get("completed"),
                "username": user[0].get("username")} for temp in todos]
            }
    with open('{}.json'.format(sys.argv[1]), 'w') as json_file:
        json.dump(dict_to_write, json_file)
