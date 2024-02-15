#!/usr/bin/python3
"""It query a list of all hot posts on given Reddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    list containing titles of all hot articles for given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    result = recurse("programming")
    if result is not None:
        print(len(result))
    else:
        print("None")
