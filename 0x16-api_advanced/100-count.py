#!/usr/bin/python3
"""Count the occurences of word in title"""
import requests


def count_words(subreddit, word_list, after='', count=None):
    """Calculate the frequency of a specific word within a set of titles"""
    if count is None:
        count = {}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    user = {'User-Agent': 'programmerhope'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if not response.ok or response.status_code == 302:
        return None
    data = response.json().get('data', {})
    after = data.get('after')
    for post in data.get('children', []):
        title_words = post['data']['title'].casefold().split()
        for word in title_words:
            if word in map(str.casefold, word_list):
                count[word] = count.get(word, 0) + 1
    if after:
        count_words(subreddit, word_list, after, count)
    else:
        sorted_count = dict(sorted(count.items(), key=lambda x: (-x[1], x[0])))
        for k, v in sorted_count.items():
            if v > 0:
                print(f'{k}: {v}')
