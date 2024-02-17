#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent to avoid potential issues

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, requests.RequestException):
        # Invalid subreddit or error during request
        return 0

# Test the function
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))


        # Check if the response contains valid data structure
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            print("Invalid response format.")
            return 0

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 403:
            print("Subreddit is blocked or private.")
        else:
            print("HTTP Error occurred:", http_err)
        return 0
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0  # Return 0 if there's an issue with the request

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py subreddit_name")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print("Number of subscribers:", subscribers)
