#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users".format(url),
                        params={'id': sys.argv[1]}).json()
    todos = requests.get("{}todos".format(url),
                         params={'userId': sys.argv[1]}).json()

    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='unix')
        for temp in todos:
            writer.writerow([sys.argv[1], user[0].get("username"),
                            temp.get("completed"), temp.get("title")])
