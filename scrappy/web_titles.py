#encoding: utf-8

import requests
from bs4 import BeautifulSoup as bs

class WebTitleSpider():

	def __init__(self):
		self.urls = [
			("https://www.amazon.co.jp/",),
			("https://www.python.org/",),
			("https://www.w3.org/",),
		]

	def get_titles(self):
		pagecontents = (bs(requests.get(url).text, 'lxml') for url in self.urls)
		return (page.title for page in pagecontents)

if __name__ == "__main__":
	urls = []
	spider = WebTitleSpider()
	for title in spider.get_titles():
		print(title)