#!/usr/bin/python3
""" Return the top posts from reddit api """
import requests
from requests import exceptions


def top_ten(subreddit):
    """ Function to return 10 top posts of subreddit """
    User = {'User-Agent': 'JennyHadir'}
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                     format(subreddit),
                     headers=User,
                     allow_redirects=False,
                     params={'limit': 10}).json()
    try:
        posts = r.get('data').get('children')
        for post in posts:
            title = post.get('data').get('title')
            print(title)
    except Exception:
        print('None')
