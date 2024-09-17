#!/usr/bin/env python3

import sys
import requests
import re
from bs4 import BeautifulSoup
from .. constants import (KWARG_URL,
                          KWARG_RESULTS_FILE,
                          KWARG_TAG,
                          KWARG_TARGET_ATTRS,
                          KWARG_PATTERN)

def validateUrl(url):
    if url is None or not url:
        raise ValueError('Invalid argument (url) can not be NoneType or empty')

def validateResultFileName(resultsFile):
    if resultsFile is None or not resultsFile:
        return 'result.txt'
    return resultsFile

def unpackArgs(kwargs):
    return [kwargs.get(KWARG_URL),
            kwargs.get(KWARG_RESULTS_FILE),
            kwargs.get(KWARG_TAG),
            kwargs.get(KWARG_TARGET_ATTRS),
            kwargs.get(KWARG_PATTERN)]

def writeContentToFile(content):
    with open('batch_file.txt', 'a') as batchFile:
        batchFile.write('{content}\n'.format(content=content))
        batchFile.close()

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
    [url, resultsFile, tag, targetAttributes, pattern] = unpackArgs(args)
    validateUrl(url)
    resultsFile = validateResultFileName(resultsFile)
    
    res = getPage(url)
    targetedContent = parseResponseForTargetField(res, tag, targetAttributes, pattern)    
    writeContentToFile(targetedContent, resultsFile)