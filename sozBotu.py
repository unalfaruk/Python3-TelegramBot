import requests

url="http://guzelsozlerblog.com/gunun-sozu"

response=requests.get(url)

print(response.text)
