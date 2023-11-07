#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        return json.get('data').get('subscribers')
    else:
        return 0
