#!/usr/bin/python3
'''
    a function that queries the Reddit API print the titles
    of the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    """method doc"""
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
