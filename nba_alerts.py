from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import numpy as np


url = 'http://www.espn.com/nba/transactions'
uClient = req(url)#opening connection, grabbing page
page_html = uClient.read()
uClient.close()#close connection
page_soup = soup(page_html, "html.parser") #parsing html page_html

#week_news = page_soup.findAll("div", {"class":"col-main", "id":"my-teams-table"})
week_news = page_soup.findAll("table", {"cellspacing":"1", "cellpadding":"3", "class":"tablehead"})

x = 1
while x < len(week_news[0].text):
	if week_news[0].text[x-1] == '7':
		print()
		x+=1
	else:
		print(week_news[0].text[x-1], end="")
		x+=1





