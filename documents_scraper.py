#!/usr/bin/env python3

import time
import requests
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup

page_numbers = 20 # Pages in the website
i = 1 # Index

# Loop through each page on the website
while i <= page_numbers:
	print("PAGE "+str(i))
	URL = ("https://www.sppra.co.sz/sppra/award_intention.php?page=" + str(page_numbers))
	page = requests.get(URL)
	soup = BeautifulSoup(page.content,"html.parser")
	results = soup.find(id = "post-list")

	#Get the links to download and download files
	links = results.find_all("a")

	# Go through each link and download file
	for link in links:
		link_url = "https://www.sppra.co.sz/sppra/" + link["href"]	
		a = urlparse(link_url)

		# Downloading Files with a delay of 30 seconds
		print("Downloading.............")
		response = requests.get(link_url)
		open((f"{os.path.basename(a.path)}"),"wb").write(response.content)
		print("Done")
		time.sleep(30)
	i = i + 1


