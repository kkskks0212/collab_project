import requests
import json
import dotenv

def getdata(url):
    response = requests.get(url)
    return json.loads(response.text)

if __name__=='__main__':
    response = getdata(url='https://randomuser.me/api')
    print(response.get('results')[0].get('name').get('first'))