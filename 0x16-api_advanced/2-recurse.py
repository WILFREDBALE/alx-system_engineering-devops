#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    if data is None:
        return hot_list
    children = data.get('children')
    if children is None or len(children) == 0:
        return hot_list
    for child in children:
        hot_list.append(child.get('data').get('title'))
    after = data.get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
3