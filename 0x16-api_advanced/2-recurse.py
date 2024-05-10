#!/usr/bin/python3
"""Queries the Reddit API Recursively"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit.
        hot_list: A list to accumulate the titles of hot articles.
        after: A token indicating the last post retrieved
        in the previous page of results.

    Returns:
        A list containing the titles of all hot articles for subreddit.
        If no results are found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            return hot_list if hot_list else None
        else:
            if len(posts) == 1:
                return hot_list + [posts[0]["data"]["title"]]
            else:
                return recurse(subreddit,
                               hot_list + [posts[0]["data"]["title"]],
                               posts[1]["data"]["name"])
    else:
        return None
