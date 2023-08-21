import os
import tweepy
import requests
import schedule
import time


# Replace with your actual consumer key and secret
CONSUMER_KEY = ""
CONSUMER_SEC = ""

# Replace with your actual access token and secret
AUTH_ACC = ""
AUTH_SEC = ""

# Replace with your actual bearer token
BEARER = ""

# To Authenticate the user credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
auth.set_access_token(AUTH_ACC, AUTH_SEC)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Authenticate using API v2.0
client = tweepy.Client(BEARER, CONSUMER_KEY, CONSUMER_SEC, AUTH_ACC, AUTH_SEC, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("V1.1 Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# Set the file path/ Change to url (import web request if required)
file_path = "/Users/yeiterilsosingkoireng/Desktop/assign/myvid/toreply.mp4"
status_text = "oh really check this out!!"

# Media upload through API v1.1
media_info = api.media_upload(filename=file_path)

# Set bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAACzGoQEAAAAAPBUyxZyXrtNzab8B3guBR9e994k%3DDieBbwNezSIZ26haV9I17LcWMpOf2z7nPkC9gYKFJEwL0AnTF3"

# Set endpoint URL
endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

def get_request():
    # Specify a search query for original tweets from @johnlemonnft, and any additional fields that are required
    params = {
        'query': 'from:DogePoundTreats -is:reply -is:retweet',
        'tweet.fields': 'author_id'
    }

    headers = {
        "User-Agent": "v2RecentSearchPython",
        "Authorization": f"Bearer {bearer_token}"
    }

    response = requests.get(endpoint_url, params=params, headers=headers)
    response_json = response.json()

    if response.status_code == 200:
        return response_json
    else:
        raise Exception('Unsuccessful request')

# Function to run the task
def run_twitter_task():
    try:
        # Make request and post reply
        response = get_request()
        if 'data' in response and len(response['data']) > 0:
            tweet = response['data'][0]
            if 'text' in tweet and 'id' in tweet:
                tweet_text = tweet['text']
                tweet_id = tweet['id']
                print("Tweet ID:", tweet_id)

                # Tweet posting through API v2.0
                try:
                    tweet = client.create_tweet(text=status_text, media_ids=[media_info.media_id], in_reply_to_tweet_id=tweet_id)
                    print("Reply posted successfully.")
                except Exception as e:
                    print(f"Error during reply posting: {e}")

    except Exception as e:
        print(e)

# A time schedule running the loop after every 20 min
schedule.every(20).minutes.do(run_twitter_task)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
