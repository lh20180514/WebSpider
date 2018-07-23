import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Host':'www.zhihu.com',
    'Cookie':'d_c0="AFDkrg7StA2PTmpF3zo65byaN79ixFddLmU=|1528252960"; _zap=ac2b6697-bb74-48db-9479-86b049b1c8a2; _xsrf=9082d119-d986-485e-bbcf-734518ee1766; l_n_c=1; n_c=1; q_c1=acb3aec912c44a958e1c62c18cca0c6a|1531355770000|1528252960000; l_cap_id="NDU1OGU0NWM5MzNjNDhjNGFmYzFhMjJlY2FhMTIzNzM=|1531905218|d6cdf49a50a199a811f05ac8153f4f23f74057bc"; r_cap_id="NjI4OGExZGUzOTA3NGEyZjlkM2M4YTNmYzEyNDI5ZmU=|1531905218|34d2defc649aad2191b309c224762aefabf2f7bf"; cap_id="ODY5ZDEzMGY3MWRiNDY4ODljOWMyZjdjYTUzOGY5ZmE=|1531905218|573c9deb1132a0251eb4c67dc202ba18afdf3c5c"; __utma=51854390.1020421846.1531905231.1531905231.1531905231.1; __utmc=51854390; __utmz=51854390.1531905231.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20180606=1; tgw_l7_route=27a99ac9a31c20b25b182fd9e44378b8; capsion_ticket="2|1:0|10:1531907505|14:capsion_ticket|44:MGZmOWQyMjIzYzdmNDQ2MGFlZGIyMjJiMTM3MTc0MzU=|2a67232ba28ad32f9a0d5b985848772bbf40aa2fd47c48cf66fe37410d544b32"; z_c0="2|1:0|10:1531907598|4:z_c0|92:Mi4xN3lsMEJnQUFBQUFBVU9TdUR0SzBEU1lBQUFCZ0FsVk5EbHc4WEFEZlFiS3JXa096ZDlZTFhiLVJFWUJmRHZiZVp3|73f83de9d5875da75b7bd347577117e76139366759541c5514a6e1eb05f19ace"; unlock_ticket="AIBCltNIpgwmAAAAYAJVTRYVT1v_6r_Eu_LkdUJ2lZJ1hn2XRl6JvA=="',
}

headers1 = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Host':'www.dyyy120.com',
    'Cookie':'__RequestVerificationToken=CdCDIoZxhWMbJyRDgRwUXhDbnvDc4x5XYdSs2vMZOwCrGWACwexImYtrPspTwhIKJZTjpZoUJLCfhCUIpNShxrFk_gtdtN2Kl4llXdACK4E1; ASP.NET_SessionId=5zunguwzzdon1f0uq31rqdml; User=UserName=lh8229238&Password=lh301415926; HBHOSPITALCODE=3820'
}

# r = requests.get('http://www.zhihu.com',headers=headers)
r = requests.get('http://www.dyyy120.com',headers=headers1)
print(r.text)
