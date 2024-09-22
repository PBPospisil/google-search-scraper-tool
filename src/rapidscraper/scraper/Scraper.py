#!/usr/bin/env python3

import sys
import requests
import re
from bs4 import BeautifulSoup
from .. constants import (TARGET_URL,
                          TARGET_TAG,
                          TARGET_ATTRS,
                          TARGET_PATTERN,
                          RESULTS_FILENAME)

def validateUrl(url):
    if url is None or not url:
        raise ValueError('Invalid argument (url) can not be NoneType or empty')

def unpackArgs(kwargs):
    return [kwargs.get(TARGET_URL),
            kwargs.get(TARGET_TAG),
            kwargs.get(TARGET_ATTRS),
            kwargs.get(TARGET_PATTERN),
            kwargs.get(RESULTS_FILENAME)]

def writeContentToFile(content, resultsFile='results.txt'):
    with open(resultsFile, 'a') as batchFile:
        batchFile.write('{content}\n'.format(content=content))
        batchFile.close()

def attemptAltPatterns(soup, pattern):
    return soup.find(text=re.compile(pattern))

def attemptWithAttrs(soup, tag, targetAttributes):
    return soup.find(tag, attrs=targetAttributes)    

def getPage(url):
    return requests.get(url)
        
def parseResponseForTargetField(response, tag='div', targetAttributes={}, pattern=''):
    soup = BeautifulSoup(response.content, 'html5lib', from_encoding='utf-8')

    html = attemptWithAttrs(soup, tag, targetAttributes)
    if html and html is not None:
        return html.contents[0]
    
    html = attemptAltPatterns(soup, pattern)
    if html: return html

    return None

def scrape(args):
    [url, tag, targetAttributes, pattern, resultsFile] = unpackArgs(args)

    validateUrl(url)
    targetedContent = parseResponseForTargetField(getPage(url), tag, targetAttributes, pattern)

    if resultsFile is None or not resultsFile:
        print(targetedContent)
    else:
        writeContentToFile(targetedContent, resultsFile)