#!/usr/bin/python3
import requests
"""
get subs for a subreddit
"""


def number_of_subscribers(subreddit):
    """
        function to get json response
    """
    api = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    head = {"User-Agent": user_agent}
    req = requests.get(api, headers=head).json()

    dat = req.get('data')
    if dat:
        subs = dat.get('subscribers')
        if subs:
            return subs
    return 0
