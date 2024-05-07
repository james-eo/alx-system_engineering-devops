#!/usr/bin/python3
"""Recursively queries the Reddit API"""

import requests
import re


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit: The name of the subreddit.
        word_list: A list of keywords to count.
        after: A token indicating the last post retrieved
            in the previous page of results.
        counts: A dictionary to store the counts of keywords.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            if counts:
                print_counts(counts, sorted(counts.items(),
                             key=lambda x: (-x[1], x[0])))
            return
        else:
            title = posts[0]["data"]["title"]
            words = re.findall(r'\b\w+\b', title.lower())
            update_counts(words, word_list, counts)
            after = data["data"]["after"]
            count_words(subreddit, word_list, after, counts)
    else:
        return


def update_counts(words, word_list, counts):
    """
    Updates the counts dictionary with occurrences
    of keywords in the given words list.

    Args:
        words: A list of words to search for keywords.
        word_list: A list of keywords to count.
        counts: A dictionary to store the counts of keywords.
    """
    if not words:
        return

    word = words.pop()
    if word.lower() in word_list:
        counts[word.lower()] = counts.get(word.lower(), 0) + 1
    update_counts(words, word_list, counts)


def print_counts(counts, sorted_counts, index=0):
    """
    Recursively prints the sorted count of keywords in descending order
    by count and ascending order alphabetically
    for keywords with the same count.

    Args:
        counts: A dictionary containing the counts of keywords.
        sorted_counts: A list of tuples containing sorted counts of keywords.
        index: Current index in the sorted counts list.
    """
    if index == len(sorted_counts):
        return

    word, count = sorted_counts[index]
    print(f"{word}: {count}")
    print_counts(counts, sorted_counts, index + 1)
