#!/usr/bin/python3
"""Module to request data from an Reddit API"""
import json
from urllib.request import Request, urlopen


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                print(data['data']['subscribers'])
            else:
                print(0)
    except Exception as e:
        print(0)
