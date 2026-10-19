import requests


Data = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(Data.json())
