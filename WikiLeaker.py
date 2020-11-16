#!/usr/bin/env python3


import sys
import time
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd


def banner():
    print('   __      __.__ __   .__.__         __         ')
    print('  /  \    /  \__|  | _|__|  |   ____ _____  |  | __ ___________ ')
    print('  \   \/\/   /  |  |/ /  |  | _/ __ \\__  \ |  |/ // __ \_  __ \\')
    print('   \    /|  |    <|  |  |_\  ___/ / __ \|    <\  ___/|  | \/')
    print('    \__/\  / |__|__|_ \__|____/\___  >____  /__|_ \\___  >__|   ')
    print('     \/      \/        \/     \/     \/    \/       ')
    print('\n')
    print('\n')
    run()


def usage():
    print('\n')
    print('Usage: python3 WikiLeaker.py <domain>')


def wikileaks(URL, REQ_VAR):
    URL_REGEX = re.compile(r"\<h4\>\<a\shref\=\"(?P<URL>https\:\/\/wikileaks\.org\S+)\"\>")
    SUBJ_REGEX = re.compile(r"\<h4\>\<a\shref\=\"https\:\/\/wikileaks\.org\S+\"\>\s(?P<subj>\S.+)\<\/a")
    SENDR1_REGEX = re.compile(r"email\:\s(?P<sender>\S.+\@\S.+\.\w{3}) ")
    SENDR2_REGEX = re.compile(r"email\:\s(?P<sender>\S+[\.|\<b\>]\w+)\<\/b\>")
    LEAK_REGEX = re.compile(r"leak\-label\"\>\n\<div\>\<b\>(?P<date>\S.+)\<\/b\>")
    DATE_REGEX = re.compile(r"Created\<br\/>\n\<span\>(?P<date>\d{4}\-\d{2}\-\d{2})")
    time.sleep(1)
    wiki_df = pd.DataFrame(columns=['Date', 'Sender', 'Subject', 'URL', 'Leak'])
    soup_var = BeautifulSoup(REQ_VAR.content, "lxml")
    divtag_var = soup_var.findAll('div', {'class': 'result'})
    for a in divtag_var:
        url_var = URL_REGEX.findall(str(a))
        date_var = DATE_REGEX.findall(str(a))
        subj_var = SUBJ_REGEX.findall(str(a))
        sendr1_var = SENDR1_REGEX.findall(str(a))
        sendrx_var = SENDR2_REGEX.findall(str(a))
        leak_var = LEAK_REGEX.findall(str(a))
        sendr2_var = re.sub(r'\<b\>', '', str(sendrx_var))
        if sendr1_var:
            sendr_var = sendr1_var
        elif sendr2_var:
            sendr_var = sendr2_var
        wiki_df = wiki_df.append({'Date': date_var, 'Sender': sendr_var, 'Subject': subj_var, 'URL': url_var, 'Leak': leak_var}, ignore_index=True, sort=True)
    for index, r in wiki_df.iterrows():
        date_var = r['Date']
        sendr_var = r['Sender']
        subj_var = r['Subject']
        url_var = r['URL']
        leak_var = r['Leak']
        print('************************************************************')
        print(f'Date: {date_var}')
        print(f'Sender: {sendr_var}')
        print(f'Subject: {subj_var}')
        print(f'URL: {url_var}')
        print(f'Leak: {leak_var}')
        print('************************************************************')


def continuer():
    r_epetite = input('Repeat? (Y/N)')
    if r_epetite.lower() == 'y':
        s_domain = input('Same domain? (Y/N)')
        if s_domain.lower() == 'y':
            wikileaks(REQ_VAR)
        else:
            n_domain = input('Enter a new domain...\t')
            VALIDATION_REGEX = re.compile(r"(?P<domain>\w+\.\w{2,6})")
            validation_check = VALIDATION_REGEX.findall(str(n_domain))
            if validation_check:
                URL = 'https://search.wikileaks.org/advanced?order_by=newest_document_date&exact_phrase='+n_domain+'&include_external_sources=True'
                print(URL)
                wikileaks(URL, REQ_VAR)
                continuer()
    else:
        exit()

def run():
    try:
        DOMAIN = sys.argv[1]
        if DOMAIN == '-h':
            usage()
        elif DOMAIN == '--help':
            usage()
        else:
            VALIDATION_REGEX = re.compile(r"(?P<domain>\w+\.\w{2,6})")
            validation_check = VALIDATION_REGEX.findall(DOMAIN)
            if validation_check:
                page_count = 1
                while True:
                    URL = 'https://search.wikileaks.org/?query=&exact_phrase=' + DOMAIN + \
                          '&include_external_sources=True&order_by=newest_document_date&page=' + str(page_count)
                    print(URL)
                    REQ_VAR = requests.get(URL)
                    wikileaks(URL, REQ_VAR)
                    page_count += 1
                continuer()


    except Exception as error_code:
        usage()
        #print(error_code)


banner()
