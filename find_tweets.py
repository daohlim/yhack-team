import requests
from requests_oauthlib import OAuth1
import json
import urllib.parse

CONSUMER_API_KEY = 'wQbdzvNEOcMOe12z77Y6Miqvc'
CONSUMER_API_SECRET = 's5DEhz0Amr5Ey8pgZWNeDiwY9BF1yEcosh2S2IFeUIP4LBBtPT'
ACCESS_TOKEN = '628291152-pbJZ0i8mGVxwmWzgPsVztZXxT4S8TaRF7ghC0icK'
ACCESS_TOKEN_SECRET = '9F7DXNN0pXOSLIyWfz5EMJ4jqIwV6VAGaEpNNAkHUPgHL'
KEYWORDS = ['the', 'i', 'a', 'to']

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(CONSUMER_API_KEY, CONSUMER_API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def find_tweets(lat, lon):
    results_arr = []
    for i in KEYWORDS:
        x = find_keyword_tweets(lat, lon, i)
        if x is not -1:
            results_arr += x
        else:
            print("Error looking for " + i)

    return results_arr


def find_keyword_tweets(lat, lon, keyword):
    url = ('https://api.twitter.com/1.1/search/tweets.json?q=' + keyword + '&result_type=recent&lang=en&count=50&'
           + 'geocode=' + str(lat) + ',' + str(lon) + ',80km')
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        loaded_json = json.loads(response.content)
        statuses = loaded_json["statuses"]
        return statuses
    else:
        print("GET Error with twitter API")
        print(response.content)
        return -1


def find_sentiment(tweet_json):
    return 1


find_tweets(1.357918, 103.800260)
