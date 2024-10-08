"""
Author: liicodex
Date: 28 July 2024
Reason: Im just geeking out at this point. im also getting ready to work on that webscraper.
"""

# REQUIRED MODULES
import schedule
import time
import tweepy
import requests as rq
import random

# THE LOGIC FUNCTIONS
def post_to_twitter(content):
    # Authenticate to Twitter (replace with your credentials)
    auth = tweepy.OAuthHandler("API_KEY", "API_SECRET_KEY")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
    api = tweepy.API(auth)
    
    # Create a tweet
    api.update_status(content)
    print("Posted to Twitter:", content)

def getRandomJoke():
    # List of categories
    categories = ["Puns", "Knock-knock", "One-liners", "Sarcastic", "Wordplay", "Wit", "Observational", "Satire", "Food", "Travel", "Animal"] #Shaggy dog stories, Play on expectation
    # Select random category
    randomCategory = random.choice(categories)

def blacklistFlags():
    # List of blacklisted flags
    blacklist = ["nsfw", "religious", "political", "racist", "sexist", "explicit"]
    chosenBlackList = []
    for i range(1, 3):
        chosenBlackList.append(blacklist[random.randint(len(blacklist))])



    # API Endpoint Handling
    url = f"https://v2.jokeapi.dev/joke/{randomCategory}?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    try:
        # Fetch joke json (GET)
        response = rq.get(url)
        
        response.raise_for_status()

        data = response.json()

        if data['type'] == 'single':
            joke = data['joke']
        else:
            joke = f"{data['setup']} \n {data['delivery']}"
        
        # Prints out the joke
        print(f"Category: {randomCategory} \n {joke}")
    
    # Dealing with HTTP Errors
    except rq.exceptions.HTTPError as errh:
        print (f"HTTP IS A B***CH")
    
    # Dealing with Connection Errors
    except rq.exceptions.ConnectionError as errc:
        print (f"SO WHAT IF IM NOT NOT CONNECTED TO THE INTERNET")
    
    # Dealing with Timeout Issues
    except rq.exceptions.Timeout as errt:
        print (f"TIME IS A B***CH")
    
    # Dealing with ERRORS!!!
    except rq.exceptions.RequestException as err:
        print (f"LIFE IS A B***CH")


# Schedule posts
schedule.every().day.at("08:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("10:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("12:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("14:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("16:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("18:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("20:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("22:00").do(post_to_twitter, content = getRandomJoke())
schedule.every().day.at("00:00").do(post_to_twitter, content = getRandomJoke())

while True:
    print("Bot running...")
    schedule.run_pending()
    time.sleep(1)
