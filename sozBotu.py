import requests
from bs4 import BeautifulSoup

url="http://guzelsozlerblog.com/gunun-sozu"

response=requests.get(url)

AnalizEdilecekIcerik=response.text #get HTML code of URL

icerigiAl=BeautifulSoup(AnalizEdilecekIcerik,"lxml") #read and analyze HTML code of url
#we use "lxml" because, when it wasn't there, there was an error. Code was running but we don't want to see warning :)
#warning text said this parameter to me. You can read this URL for parameters: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

filtre=icerigiAl.find_all(id="PageContent") #Filter HTML code which analyzed for just div tags
print(filtre)
print(filtre[0])
