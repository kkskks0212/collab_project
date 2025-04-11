import pandas as pd
import requests
import json
import requests
import json
import dotenv

def getdata(url):
    response = requests.get(url)
    return response.json()

if __name__=='__main__':
    response = getdata(url='https://randomuser.me/api')

df = pd.json_normalize(response["results"])


df = df[['name.first', 'name.last', 'location.city', 'location.state', 'location.country', 'location.postcode', 'location.coordinates.latitude', 'location.coordinates.longitude', 'email', 'login.uuid', 'dob.date', 'dob.age', 'registered.date', 'registered.age', 'phone', ]]
df.columns = ['first_name', 'last_name', 'city', 'state', 'country', 'postcode', 'latitudes', 'longitudes', 'email', 'id', 'DOB', 'age', 'registration_date', 'age_while_registeration', 'phone']
for _ in range(100):
    response = getdata(url='https://randomuser.me/api')
    new_data = pd.json_normalize(response["results"])
    new_data = new_data[['name.first', 'name.last', 'location.city', 'location.state', 'location.country', 'location.postcode']]
    new_data.columns = ['first_name', 'last_name', 'city', 'state', 'country', 'postcode']

    df = pd.concat([df, new_data], ignore_index=True)


print(df)




