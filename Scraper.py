#!/usr/bin/env python3

import sys
import requests
import re
from bs4 import BeautifulSoup
from services import writeContentToFile

def attemptAltPatterns(soup, pattern, tag, tagAttributes):
    print(soup)
    html = soup.find(tag, class_=tagAttributes)
    if html and html is not None:
        return html.contents[0]
    
    html = soup.find_all(text= re.compile(pattern))
    if html:
        return html
    
    return None

def getPage(url):
    return requests.get(url)
        
def parseResponseForTargetField(response, pattern, tag, tagAttributes):
    soup = BeautifulSoup(response.content, 'html5lib', from_encoding='utf-8')
    return attemptAltPatterns(soup, pattern, tag, tagAttributes)

def scrape(url, tag, tagAttributes, pattern):
    res = getPage(url)
    targetedContent = parseResponseForTargetField(res, pattern, tag, tagAttributes)    
    writeContentToFile(targetedContent)

if __name__ == '__main__':
    scrape(**dict(arg.split('=') for arg in sys.argv[1:]))