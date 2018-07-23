import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

r = requests.get('http://httpbin.org/get?name=germey&age=22')
print(r.text)

data = {'name':'germey','age':22}
r = requests.get('http://httpbin.org/get',params=data)
print(r.json())