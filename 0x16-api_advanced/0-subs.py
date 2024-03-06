#!/usr/bin/python3
"""Module to request data from an Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
    return res.get('data', {}).get('subscribers', 0)
