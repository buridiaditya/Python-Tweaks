from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import re

url = "https://icann562016.sched.org/"
html1 = requests.get(url)
soup = BeautifulSoup(html1.content)
primaryLinks = soup.find_all('a',class_="name")
secondaryLinks = []

for link in primaryLinks:
	secondaryLinks.append( url[0:len(url) - 1] + link.get('href') + '/')

print ("Searching PDF files:")

for link in secondaryLinks:
	html = requests.get(link)
	newSoup = BeautifulSoup(html.content)
	pdfLinks = newSoup.find_all('a',class_="file-uploaded file-uploaded-pdf") 
	for pdf in pdfLinks:
		count = 0
		print ("Downloading " + pdf.get('href') + ":")
		urllib.request.urlretrieve(pdf.get('href'),pdf.string)
		print (pdf.string + " Downloaded Succesfully!")
		# convertion int bash style string
		fileName = ""
		for i in pdf.string:
			if i == " " :
				fileName = fileName + "\ "
			elif i == "&":
				fileName = fileName + "\&"
			else:
				fileName = fileName + i
		print (fileName)
		os.system("pdftotext " + fileName)
		print ("Convertion to txt succesfull!")
		fileRead = open(pdf.string + ".txt").read().lower()
		fileData = re.split(',|\.| ',fileRead)
		for i in fileData:
			if i == "jurisdiction":
				count += 1
		print (count)
print ("All Downloads Complete!!")




	