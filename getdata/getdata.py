import requests
import json
import dotenv

def getdata(url):
    response = requests.get(url)
    return json.loads(response.text)
