import requests

r = requests.get('http://www.dyyy120.com/')

# print(type(r))
print(r.status_code)
print(r.text)
print(r.cookies)
