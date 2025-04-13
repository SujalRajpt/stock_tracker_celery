import requests

url = "https://finance.yahoo.com/quote/CIPLA.NS"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
print(res.status_code)
print(res.text[:1000])
