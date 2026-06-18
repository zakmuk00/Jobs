import requests
import os
import json

key = os.environ.get('FINDWORK_KEY')
url = 'https://findwork.dev/api/jobs/'

headers = {
  'Authorization' : f'Token {key}'
}

tags = {
  'employment_type' : 'internship',
  'location' : None,
  'remote' : None,
  'url' : None
}

response = requests.get(url, headers = headers, params = tags)

if response.status_code == 200:
  data = response.json()







print(response.status_code)
print(response.json())
