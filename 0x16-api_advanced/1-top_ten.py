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

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for child in children[:10]:
                    title = child.get("data", {}).get("title")
                    if title:
                        print(title)
        else:
            print("No posts found for this subreddit.")
    else:
        print("None")
