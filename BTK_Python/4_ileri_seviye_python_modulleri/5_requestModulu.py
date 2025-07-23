import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
#print(response)

text = json.loads(response.text)
print(text[0])
print(text[0]['title'])

for item in text:
    if item['userId'] == 1:
        print(item['title'])