#!/usr/bin/env python3

import sys
import requests
import re
from bs4 import BeautifulSoup
from services import writeContentToFile

def attemptAltPatterns(soup, pattern):
    return soup.find_all(text=re.compile(pattern))

def attemptWithAttrs(soup, targetAttributes):
    return soup.find(targetAttributes.get('tag'), attrs=targetAttributes)    

def getPage(url):
    return requests.get(url)
        
def parseResponseForTargetField(response, targetAttributes, pattern):
    soup = BeautifulSoup(response.content, 'html5lib', from_encoding='utf-8')

    html = attemptWithAttrs(soup, targetAttributes)
    if html and html is not None:
        return html.contents[0]
    
    html = attemptAltPatterns(soup, pattern)
    if html: return html

    return None

def scrape(url, tag='div', targetAttributes={}, pattern=''):
    res = getPage(url)
    targetedContent = parseResponseForTargetField(res, tag, targetAttributes, pattern)    
    writeContentToFile(targetedContent)

if __name__ == '__main__':
    scrape(**dict(arg.split('=') for arg in sys.argv[1:]))