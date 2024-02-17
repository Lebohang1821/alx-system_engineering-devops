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
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url['data']['subscribers']  # Accessing dictionary directly
    except KeyError:
        print("Subreddit not found or private.")
        return 0  # Return 0 for non-existing or private subreddit
    except Exception as e:
        print("An error occurred:", e)
        return 0  # Return 0 for any other error


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py subreddit_name")
    else:
        subscribers = number_of_subscribers(argv[1])
        print("Number of subscribers:", subscribers)
