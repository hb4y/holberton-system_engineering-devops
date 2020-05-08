#!/usr/bin/python3
"""
get top 10 post of subreddit
"""


import requests


def top_ten(subreddit):
    """
        function to get json response
    """
    api = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    head = {"User-Agent": user_agent}
    response = requests.get(api, headers=head)

    if not response:
        return None

    for i in range(10):
        dat = response.json().get('data') \
              .get('children')[i].get('data').get('title')
        if dat:
            print(dat)
