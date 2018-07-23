import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

r = requests.get('http://www.dyyy120.com',headers=headers)
# print(r.cookies)

for key, value in r.cookies.items():
    print(key + "=" + value)