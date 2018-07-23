import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
r = s.get('http://httpbin.org/cookies')
print(r.text)