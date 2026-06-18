import requests
import json

url = 'https://www.arbeitnow.com/api/job-board-api'

response = requests.get(url)

print(response.json())

