import requests
from bs4 import BeautifulSoup

url="http://guzelsozlerblog.com/gunun-sozu" #Our url which will we read

response=requests.get(url) #Go to URL
response.encoding= "iso-8859-9" #Web site's charset --> <meta http-equiv="content-type" content="text/html; charset=iso-8859-9">
#Encoding is important for your text's characters which get from website

AnalizEdilecekIcerik=response.text #get HTML code of URL

icerigiAl=BeautifulSoup(AnalizEdilecekIcerik,"lxml") #read and analyze HTML code of url
#we use "lxml" because, when it wasn't there, there was an error. Code was running but we don't want to see warning :)
#warning text said this parameter to me. You can read this URL for parameters: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

#Filter HTML code which analyzed with CSS selector for just div tags
sozler=icerigiAl.select("div#PageContent") #get div containers

gonderilecekYazi="" #we will sent this to telegram chat

for i in range(0,len(sozler)): #iterate from 0 to length of our list
    gonderilecekYazi+=sozler[i].contents[0].text +": "+sozler[i].contents[2]+"\n\n"

token = "309763441:AAGSg428wxoneR82YrFphrphqmr6n97cz_Y" #telegram token
chat_id = "253529798" #telegram id

requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': 253529798, 'text': gonderilecekYazi}).json()
#telegram sendMessage url, more commands --> https://core.telegram.org/bots