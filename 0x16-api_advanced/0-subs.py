#!/usr/bin/python3
""" Return the number of subscribers from reddit api """
import requests


def number_of_subscribers(subreddit):
    """ Function to get number of subreddit subscribers """
    User = {'User-Agent': 'JennyHadir'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit),
                     headers=User).json()
    if req.status_code == 200:
        data = r.get('data')
        subscribers = data.get('subscribers')
        if data is not None and subscribers is not None:
            return subscribers
    return 0
