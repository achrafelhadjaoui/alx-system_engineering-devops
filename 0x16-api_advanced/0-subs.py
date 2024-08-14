#!/usr/bin/python3
'''
    a function that queries the Reddit API and returns the number
    subscribes (not active user, total subscribers) for a given
    subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    return 0
