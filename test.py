import requests
import pandas as pd
import json
import ast
import yaml

def create_twitter_url():
    handle = 'Billius27'
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle) 
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(mrf, q)
    return url

def process_yaml():
    with open("config.yaml") as file:
        return yaml.safe_load(file)

def create_bearer_token(data):
    return data['search_tweets_api']['bearer_token']

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()