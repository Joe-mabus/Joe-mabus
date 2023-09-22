import requests
import pandas as pd
import json as js

url = 'https://performance.cookcountyil.gov/resource/76gh-xye3?$limit=2000&$offset=0'
head = {'Accept' : 'application/json', 'Host' : 'performance.cookcountyil.gov'}

r = requests.get(url, headers = head)

reports = r.json()

df = pd.DataFrame(reports)

race_data = df['race'].astype('str')

print(race_data.value_counts())

exit() 


df.info()

''' Socrata Access Method
from sodapy import Socrata
client = Socrata("performance.cookcountyil.gov", None)

client = Socrata("performance.cookcountyil.gov",
                app_token,
                 username="jmabus@gmail.com",
                 password="C00kc0untyG0v!")
r = client.get("76gh-xye3", limit=2000)
'''

''' Other observation commands
df['column'] = df['column'].astype('str')

print(df.iloc[:5,:5])

print(race_data.value_counts())
'''

''' Experimenting with functions
for c in df.columns:
    if df[c].dtype == object:
        print "convert ", df[c].name, " to string"
        df[c] = df[c].astype(str)       
'''
