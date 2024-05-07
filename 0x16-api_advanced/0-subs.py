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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json().get("data").get("subscribers")
        return subscribers
    else:
        return 0
