#!/usr/bin/python3
"""Fetch and list titles of all hot posts on a subreddit via Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Retrieve titles of all currently hot posts from a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    headers = {'User-Agent': 'Test123'}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if not response.ok:
        return None
    data = response.json().get('data', {})
    after = data.get('after')
    hot_list.extend(post['data']['title'] for post in data.get('children', []))
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
