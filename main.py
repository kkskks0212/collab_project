import requests
import json
import dotenv

def getdata(url):
    response = requests.get(url)
    return response.text

if __name__=='__main__':
    response = getdata(url='https://randomuser.me/api')
    print(response)