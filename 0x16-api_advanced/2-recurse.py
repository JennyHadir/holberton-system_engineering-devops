#!/usr/bin/python3
""" Return the top posts from reddit api """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Function to return 10 top posts of subreddit """
    User = {'User-Agent': 'JennyHadir'}
    r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                     format(subreddit, after),
                     headers=User,
                     allow_redirects=False).json()

    data = r.get('data')
    after = data.get('after')
    posts = data.get('children')
    if posts is not None:
        for post in posts:
            title = post.get('data').get('title')
            hot_list.append(title)
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        if hot_list is None:
            return None
        return hot_list
