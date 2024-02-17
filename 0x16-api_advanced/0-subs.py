#!/usr/bin/python3
'''
    It contains function number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        It returns number of subscribers for given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    try:
        url = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=user)
        url.raise_for_status()  # Raise an exception for bad status codes
        data = url.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0  # Return 0 if there's an issue with the request
    except KeyError:
        print("Subreddit not found or private.")
        return 0  # Return 0 for non-existing or private subreddit


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py subreddit_name")
    else:
        subscribers = number_of_subscribers(argv[1])
        print("Number of subscribers:", subscribers)
