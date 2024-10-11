"""
Author: liicodex
Date: 28 July 2024
Reason: Simplified and improved version of the joke bot.
"""

import time
import tweepy
import requests
import random

# Twitter API credentials
TWITTER_CREDENTIALS = {
    "API_KEY": "YOUR_API_KEY",
    "API_SECRET_KEY": "YOUR_API_SECRET_KEY",
    "ACCESS_TOKEN": "YOUR_ACCESS_TOKEN",
    "ACCESS_TOKEN_SECRET": "YOUR_ACCESS_TOKEN_SECRET"
}

JOKE_API_URL = "https://v2.jokeapi.dev/joke/{category}?blacklistFlags={blacklist}"
CATEGORIES = ["Puns", "Knock-knock", "One-liners", "Sarcastic", "Wordplay", "Wit", "Observational", "Satire", "Food", "Travel", "Animal"]
BLACKLIST = ["nsfw", "religious", "political", "racist", "sexist", "explicit"]

def authenticate_twitter():
    auth = tweepy.OAuthHandler(TWITTER_CREDENTIALS["API_KEY"], TWITTER_CREDENTIALS["API_SECRET_KEY"])
    auth.set_access_token(TWITTER_CREDENTIALS["ACCESS_TOKEN"], TWITTER_CREDENTIALS["ACCESS_TOKEN_SECRET"])
    return tweepy.API(auth)

def post_to_twitter(api, content):
    try:
        api.update_status(content)
        print("Posted to Twitter:", content)
    except tweepy.TweepError as e:
        print(f"Error posting to Twitter: {e}")

def get_random_joke():
    category = random.choice(CATEGORIES)
    blacklist_params = ",".join(BLACKLIST)
    url = JOKE_API_URL.format(category=category, blacklist=blacklist_params)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['type'] == 'single':
            joke = data['joke']
        else:
            joke = f"{data['setup']}\n{data['delivery']}"

        return f"Category: {category}\n\n{joke}"
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch joke: {str(e)}"

def main():
    api = authenticate_twitter()
    while True:
        joke = get_random_joke()
        post_to_twitter(api, joke)
        time.sleep(3600)  # Wait for 1 hour before posting the next joke

if __name__ == "__main__":
    main()