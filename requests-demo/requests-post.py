import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

data = {'name':'germey','age':'22'}

r = requests.post('https://httpbin.org/post',data=data)
print(r.text)