import http.cookiejar,urllib.request

filename = 'cookies.txt'
# cookie = http.cookiejar.CookieJar()
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.dyyy120.com')
cookie.save(ignore_discard=True,ignore_expires=True)

# for item in cookie:
#     print(item.name + "=" + item.value)