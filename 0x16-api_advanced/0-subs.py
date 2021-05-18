#!/usr/bin/python3
""" Return the number of subscribers from reddit api """
import requests


def number_of_subscribers(subreddit):
    """ Function to get number of subreddit subscribers """
    User = {'User-Agent': 'JennyHadir'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit),
                     headers=User,
                     allow_redirects=False).json()
    try:
        return r.get('data').get('subscribers')
    except Exception:
        return 0
