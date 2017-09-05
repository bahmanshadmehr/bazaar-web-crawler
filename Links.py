import re
import urllib.parse

class LinkHandler:
	'''
	Seen URL is the list of downloaded URLs...
	'''
	def __init__(self, seedURL, linkRegex, junkRegex, replaceRegex, blockedRegex):
		self.seedURL = "http://" + urllib.parse.urlparse(seedURL).netloc + urllib.parse.urlparse(seedURL).path
		self.seenURL = {seedURL: 1}
		self.linkRegex = linkRegex
		self.junkRegex = junkRegex
		self.blockedRegex = blockedRegex
		self.replaceRegex = replaceRegex
		self.count = 0

	def add(self, links = [], depth = 0):
		if links:
			for each in links:
				link = self.normalize(self.seedURL, each)
				if link and (link not in self.seenURL):
					self.seenURL[link] = depth
					self.count += 1
					self.Status(str(self.count) + " Aded To Seen URLs", link)

	def check(self, url):
		url = self.normalize(self.seedURL, url)
		return url in self.seenURL

	def normalize(self, seed_url, link):
		link = urllib.parse.urldefrag(link)[0].strip() # remove hash to avoid duplicates
		link = urllib.parse.urljoin(seed_url, link)
		if not re.search(self.linkRegex, link) or re.search(self.blockedRegex, link):
			return None
		return link

	def printLinks(self):
		c = 0
		for link in self.seenURL:
			print(str(c), "--->", link)

	def countURLs(self):
		print(self.count)

	def Status(self, status, details):
		print(status, "--------> ", details)