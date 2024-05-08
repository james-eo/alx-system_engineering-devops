#!/usr/bin/python3
"""Fetches subscriber count for a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit: The name of the subreddit.

    Returns:
        The number of subscribers for the subreddit.
        If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")

#    if response.status_code == 200:
#        data = response.json()
#        subscribers = data["data"]["subscribers"]
#        return subscribers
#    return 0
