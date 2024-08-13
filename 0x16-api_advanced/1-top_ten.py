#!/usr/bin/python3
"""Module to retrieve and display titles of the top 10 most popular posts on a subreddit"""
import requests


def top_ten(subreddit):
    """Provide a list of the titles for the ten most popular posts currently on the subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    user = {'User-Agent': 'programmerhope'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    for post in response.json().get('data').get('children'):
        print(post.get('data').get('title'))
