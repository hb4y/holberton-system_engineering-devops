#!/usr/bin/python3
import requests
"""
get subs for a subreddit
"""


def number_of_subscribers(subreddit):
    api = 'https://www.reddit.com/r/{}/about.json'

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    head = {"User-Agent": user_agent}
    req = requests.get(api.format(subreddit), headers=head).json().get('data')

    if req:
        return req.get('subscribers')
    return 0
