import requests
import re

class Downloader:
	def __init__(self):
		self.requestCounter = 0

	def download(self, url):
		if re.search(r"(/list/|/deveoper/)", url):
			return self.downloadRequest(url)
		return self.downloadNormalLink(url)

	def downloadNormalLink(self, url):
		#The Link Is From linkQueue, So It's Already Normalized
		html = None
		try:
			print(url)
			html = requests.get(url)
		except Exception as e:
			html = None

		if html:
			return [html, ]
		return None

	def downloadRequest(self, link):
		responses = []
		url = requestGenerator(link)

		try:
			html = requests.get(url)
			responses.append(html)
		except Exception as e:
			self.requestCounter
			downloadRequest(link)

		if not re.search("</a>"):
			return []
		else:
			return responses + downloadRequest(link)

	def requestGenerator(self, url):
		url = url + "&partial=true&p=" + str(self.requestCounter)
		self.requestCounter += 24

		return url

	def resetRequestCounter(self):
		requestCounter = 0
