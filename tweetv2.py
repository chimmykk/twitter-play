import os
import tweepy
import requests

# Set bearer token
bearer_token = ""

# Set endpoint URL
endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

# Define your Twitter API keys and tokens. Replace the placeholders with your actual keys and tokens
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SEC = "your_consumer_secret"
AUTH_ACC = "your_access_token"
AUTH_SEC = "your_access_secret"

# Authenticate using API v1.1
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
auth.set_access_token(AUTH_ACC, AUTH_SEC)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Authenticate using API v2.0
client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

# Function to get the recent original tweet ID from a specific user
def get_request():
    # Edit query parameters below
    # Specify a search query for original tweets from a specific user (e.g., @johnlemonnft), excluding replies and retweets
    params = {
        'query': 'from:johnlemonnft -is:reply -is:retweet',
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

try:
    # Make request to get the recent original tweet ID
    response = get_request()

    # Display the first recent original tweet from @johnlemonnft with text and tweet ID
    if 'data' in response and len(response['data']) > 0:
        tweet = response['data'][0]
        if 'text' in tweet and 'id' in tweet:
            tweet_text = tweet['text']
            tweet_id = tweet['id']
            print("Tweet ID:", tweet_id)
            print("Tweet Text:", tweet_text)

           
            file_path = "/path/to/your/video.mp4"
            status_text = "Your reply message"
            # Set the path 

            # Upload media (video) through API v1.1
            media_info = api.media_upload(filename=file_path)

            try:
                tweet = client.create_tweet(text=status_text, media_ids=[media_info.media_id], in_reply_to_tweet_id=tweet_id)
                print("Reply posted successfully.")
            except Exception as e:
                print(f"Error during reply posting: {e}")
        else:
            print("No text or tweet ID found in the recent original tweet.")
    else:
        print("No recent original tweets found to reply to.")
except Exception as e:
    print(f"Error during API request: {e}")
