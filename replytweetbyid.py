import os
import tweepy

CONSUMER_KEY = ""
CONSUMER_SEC = ""

# Access token and Secret
AUTH_ACC = "1576014870084030465-eNPRHtueYUoaxKlYJKWVgtnxgzk1Jq"
AUTH_SEC = "xD9IXgJjthdxLzqn9b76i1k0GtKYT0TPeyyMdEIPhHOSl"

# Replace with your actual bearer token
BEARER = "AAAAAAAAAAAAAAAAAAAAACzGoQEAAAAAPBUyxZyXrtNzab8B3guBR9e994k%3DDieBbwNezSIZ26haV9I17LcWMpOf2z7nPkC9gYKFJEwL0AnTF3"

# Authenticate using API v1.1
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

# Set the file path and status text
file_path = "path"
status_text = "message"

# Media upload through API v1.1
media_info = api.media_upload(filename=file_path)

# Tweet posting through API v2.0
try:
    tweet_id = "tweetid"  # Replace with the specific tweet ID
    tweet = client.create_tweet(text=status_text, media_ids=[media_info.media_id], in_reply_to_tweet_id=tweet_id)
    print("Reply posted successfully.")
except Exception as e:
    print(f"Error during reply posting: {e}")
