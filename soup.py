from bs4 import BeautifulSoup
import requests
import urllib.request
import os
from socket import error as SocketError
import errno

def search(inputFile,match):
	lineNo = []
	line = 0;
	NoOfMatches = 0
	for i in inputFile:
		line += 1
		for j in range(len(i)):
			counter = 0
			for k in range(len(match)):
				if match[k] == i[j + k]:
					counter += 1
				else:
					break
			if counter == len(match):
				lineNo.append(line)
				NoOfMatches += 1
	lineNo.append(NoOfMatches)
	return lineNo

if 0:
	url = "https://icann562016.sched.org/"
	html1 = requests.get(url)
	soup = BeautifulSoup(html1.content)
	primaryLinks = soup.find_all('a',class_="name")
	secondaryLinks = []

	for link in primaryLinks:
		# os.system("mkdir " + link.string)
		# f = open("/home/buridi/Desktop/SOUP/" + "folderNames.txt","a")
		# f.write(link.string + "\n")
		link = ( url[0:len(url) - 1] + link.get('href') + '/')
		print ("Searching PDF files in: " + link)
		html = requests.get(link)
		newSoup = BeautifulSoup(html.content)
		pdfLinks = newSoup.find_all('a',class_="file-uploaded file-uploaded-pdf") 
		for pdf in pdfLinks:
			print ("Downloading " + pdf.get('href') + ":")
			urllib.request.urlretrieve(pdf.get('href'),"/home/buridi/Desktop/SOUP/" + pdf.string[0:len(pdf.string) - 1])
			print (pdf.string + "Downloaded Succesfully!!")
			filepdfs = open("/home/buridi/Desktop/SOUP/" + "pdfFileNames.txt","a")
			filepdfs.write(pdf.string[0:len(pdf.string) - 1] + "\n") 
if 1:
		# convertion int bash style string
	# openFolders = open("/home/buridi/Desktop/SOUP/" + "folderNames.txt","r")
	# for folder in openFolders:
		openFiles = open("/home/buridi/Desktop/SOUP/" + "pdfFileNames.txt","r")
		for file in openFiles:
			fileName = ""
			for i in file:
				if i in " ~`!@#$%^&*()_-+={}[]:>;',</?*-+" :
					fileName = fileName + "\\" + i 
				else:
					fileName = fileName + i
			os.system("pdftotext " + "/home/buridi/Desktop/SOUP/"  + fileName)
			fileRead = open("/home/buridi/Desktop/SOUP/" + file[0:len(file) - 1] + ".txt")
			
			# Searching
			lineNo  = search(fileRead,"jurisdiction")
			fileLog = open("/home/buridi/Desktop/SOUP/" + file[0:len(file) - 1] + "-Log.txt","a")
			fileLog.write("Total No of Matches found : " + str(lineNo[len(lineNo) - 1]) + "\n")
			if len(lineNo) > 1:
				print (file[0:len(file) - 1])
			for no in lineNo[0:len(lineNo) - 1]:
				fileLog.write("Match found in Line No :" + str (no) + "\n")
print ("All Downloads Complete!!")




	