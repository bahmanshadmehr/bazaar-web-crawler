class LinkQueue:
	def __init__(self, seedURL):
		self.seedURL = seedURL
		self.links = []
		self.counter = 0

	def add(self, link):
		self.links.append(link)
		self.counter += 1
		print(str(self.count()) + " -> Link Aded To Queu --------------------->", link)

	def count(self):
		return(self.counter)

	def pop(self):
		self.counter -= 1
		link = self.links[0]
		del(self.links[0])
		return link

	def check(self, url):
		#You Have To Normalize The Link First From LinkQueue Class In Links Module
		return url in self.links