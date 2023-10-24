#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users".format(url),
                        params={'id': sys.argv[1]}).json()
    todos = requests.get("{}todos".format(url),
                         params={'userId': sys.argv[1]}).json()

    completed = []
    for temp in todos:
        if temp.get("completed") is True:
            completed.append(temp.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(user[0].get("name"), len(completed), len(todos)))
    for title in completed:
        print("\t {}".format(title))
