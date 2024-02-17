#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
from json.decoder import JSONDecodeError

def number_of_subscribers(subreddit):
    '''
        It returns number of subscribers for given subreddit
    '''
    user_agent = {'User-Agent': 'Lizzie'}
    try:
        response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers=user_agent
        )
        response.raise_for_status()  # Raise an exception for bad status codes

        # Check if response contains valid JSON data
        try:
            data = response.json()
        except JSONDecodeError:
            print("Subreddit not found or private.")
            return 0

        # Check if the response contains valid data structure
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            print("Invalid response format.")
            return 0

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0  # Return 0 if there's an issue with the request
