#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            print("No posts found for this subreddit.")
            return
        for post in posts[:10]:
            print(post["data"]["title"])
    else:
        print(None)
