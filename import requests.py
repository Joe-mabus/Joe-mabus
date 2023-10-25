import requests
import pandas as pd
import json as js
import numpy as np

url = 'https://performance.cookcountyil.gov/resource/76gh-xye3?$limit=2000&$offset=0'
head = {'Accept' : 'application/json', 'Host' : 'performance.cookcountyil.gov'}

r = requests.get(url, headers = head)

reports = r.json()

df = pd.DataFrame(reports)

## first analysis 

from scipy.stats import chi2_contingency
cross_tab=pd.crosstab(index=df['race'],columns=df[df['gun_related'].astype('str') == 'True'])

## print(cross_tab)

chi_sq_result = chi2_contingency(cross_tab,)
p, x = chi_sq_result[1], "reject" if chi_sq_result[1] < 0.05 else "accept"
 
print(f"The p-value is {chi_sq_result[1]} and hence we {x} the null Hpothesis with {chi_sq_result[2]} degrees of freedom")

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
