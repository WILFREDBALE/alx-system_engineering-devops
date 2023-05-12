#!/usr/bin/python3
import requests
def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data')
    if not data:
        print(None)
        return
    children = data.get('children')
    if not children:
        print(None)
        return
    for i in range(min(len(children), 10)):
        print(children[i]['data']['title'])
3