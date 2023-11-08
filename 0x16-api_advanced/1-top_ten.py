#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers={"User-Agent": "Mozilla/5.0"},
                            allow_redirects=False,
                            )
    if response.status_code == 200:
        json = response.json()
        for i in range(10):
            print(json.get('data').get('children')[i].get('data').get('title'))
    else:
        print('None')
