import requests
import json

with open('request-data.json', encoding='utf-8') as f:
    data = json.load(f)

response = requests.post('https://alice-serv-kkk.herokuapp.com/post', json=data).json()
print(response)

# with open('response-data.json', mode='w', encoding='utf-8') as f:
#     f.write(json.dumps(response))
