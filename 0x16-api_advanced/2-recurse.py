#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers={"User-Agent": "Mozilla/5.0"},
                            params={"after": after,
                                    "limit": 100},
                            allow_redirects=False,
                            )
    if response.status_code == 200:
        json = response.json()
        children = json.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        after = response.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
