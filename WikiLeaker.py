#!/usr/bin/env python3
import sys
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def wikileaks(req, domain):
	urlRegex = re.compile(r"\<h4\>\<a\shref\=\"(?P<URL>https\:\/\/wikileaks\.org\S+)\"\>")
	subjRegex = re.compile(r"\<h4\>\<a\shref\=\"https\:\/\/wikileaks\.org\S+\"\>\s(?P<subj>\S.+)\<\/a")
	sendr1Regex = re.compile(r"email\:\s(?P<sender>\S.+\@\S.+\.\w{3}) ")
	sendr2Regex = re.compile(r"email\:\s(?P<sender>\S+[\.|\<b\>]\w+)\<\/b\>")
	leakRegex = re.compile(r"leak\-label\"\>\n\<div\>\<b\>(?P<date>\S.+)\<\/b\>")
	dateRegex = re.compile(r"Created\<br\/>\n\<span\>(?P<date>\d{4}\-\d{2}\-\d{2})")
	time.sleep(1)
	wikiDF = pd.DataFrame(columns=['Date', 'Sender', 'Subject', 'URL', 'Leak'])
	soup = BeautifulSoup(req.content, "lxml")
	divtag = soup.findAll('div', {'class': 'result'})
	for a in divtag:
		urll = urlRegex.findall(str(a))
		datee = dateRegex.findall(str(a))
		subj = subjRegex.findall(str(a))
		sendr1 = sendr1Regex.findall(str(a))
		sendrx = sendr2Regex.findall(str(a))
		leak = leakRegex.findall(str(a))
		sendr2 = re.sub('\<b\>', '', str(sendrx))
		if sendr1:
			sendr = sendr1
		if sendr2:
			sendr = sendr2
		else:
			sendr = 'There is no sender defined'
		wikiDF = wikiDF.append({'Date': datee, 'Sender': sendr, 'Subject': subj, 'URL': urll, 'Leak': leak}, ignore_index=True, sort=True)
	for index, r in wikiDF.iterrows():
		datee=r['Date']
		sendr=r['Sender']
		subj=r['Subject']
		urll=r['URL']
		leak=r['Leak']
		print('************************************************************')
		print(f'Date: {datee}')
		print(f'Sender: {sendr}')
		print(f'Subject: {subj}')
		print(f'URL: {urll}')
		print(f'Leak: {leak}')
	print('************************************************************')

if __name__ == "__main__":
	try:
		domain = sys.argv[1]
		url = 'https://search.wikileaks.org/?query=&exact_phrase='+domain+'&include_external_sources=True&order_by=newest_document_date'
		print(url)
		req = requests.get(url)
		result = wikileaks(req, domain)
	except Exception as e:
		print(e)
