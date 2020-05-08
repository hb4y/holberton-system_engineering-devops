#!/usr/bin/python3
"""
get subs for a subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """
        function to get json response
    """
    api = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    head = {"User-Agent": user_agent}
    response = requests.get(api, headers=head)

    dat = response.json().get('data')
    if dat:
        subs = dat.get('subscribers')
        return subs
    return 0
