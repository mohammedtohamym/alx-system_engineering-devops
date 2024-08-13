#!/usr/bin/python3
"""Module to calculate the number of users subscribed to a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Find out how many people subscribe to a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user = {'User-Agent': 'programmerhope'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get('subscribers')
