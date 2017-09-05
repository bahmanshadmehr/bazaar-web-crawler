from Links import LinkHandler
from Queue import LinkQueue
from Downloader import Downloader
import lxml.html
import re
import threading
import time
from urllib.parse import urlparse

def crawler(seedURL, firstURLs, linkRegex, junkRegex, replaceRegex, blockedRegex = None, maxThread = 10, sleepTime = 5):
	linkHandler = LinkHandler(seedURL,linkRegex, junkRegex, replaceRegex, blockedRegex)
	linkQueue = LinkQueue(seedURL)
	downloader = Downloader()

	file = open("links.txt", "w")

	for each in firstURLs:
		linkQueue.add(each)

	def linkDownloader():

		while linkQueue.count():

			url = linkQueue.pop()

			url = linkHandler.normalize(seedURL, url)

			responses = downloader.download(url)

			if responses:

				for response in responses:
					links = getAllLinksInThePage(response.content, blockedRegex)

					if not links:
						continue

					for link in links:
						if sameURL(seedURL, link):
							link = linkHandler.normalize(seedURL, link)
							if not link:
								continue
							if not linkHandler.check(link) and not linkQueue.check(link) and not (link == url):
								linkQueue.add(link)
								if re.search("/app", link):
									file.write(link + "    \n")
			linkHandler.add([url, ])
		linkHandler.countURLs()

	threads = []

	while threads or linkQueue.count() > 0:
		for thread in threads:
			if not thread.is_alive():
				threads.remove(thread)

		while len(threads) < maxThread and linkQueue.count() > 0:
			thread = threading.Thread(target = linkDownloader)
			thread.setDaemon(True)
			thread.start()
			threads.append(thread)

		time.sleep(sleepTime)

def sameURL(seedURL, url):
	if not re.search("http://", url) and not re.search("https://", url) and not re.search("www\.", url):
		return True
	return urlparse(seedURL).netloc == urlparse(url).netloc

def getAllLinksInThePage(page, blockedRegex):
	mainLinks = []

	tree = lxml.html.fromstring(page)
	links = tree.cssselect("a")

	for link in links:
		href = link.get("href")

		if blockedRegex and href:
			if not re.search(blockedRegex, href):
				mainLinks.append(href)

	return mainLinks

if __name__ == "__main__":
	crawler("https://cafebazaar.ir", ["https://cafebazaar.ir/cat/?l=en&partial=true"], "(/cat/|/pages/|/lists/|/app/|/developer/)", r"", r"", "(/s\.cafebazaar\.ir/|/redirect/|l=fa)")
