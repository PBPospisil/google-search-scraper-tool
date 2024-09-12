#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

KWARG_ORGANIZATION = 'org'
KWARG_MUNICIPALITY = 'mun'
KWARG_TAG = 'tag'
KWARG_TAG_ATTRS = 'tag_attrs'
KWARG_OPTIONAL = 'opt'

URL_PREFIX = "https://google.com/search?q="

def composeUrl(query):
    return "{url_prefix}{query}".format(url_prefix=URL_PREFIX, query=query)

def scrape(query):
    url = composeUrl(query)
    return requests.get(url)

def scrapeListing(organization, municipality):
    query = "{org}+{mun}".format(org=organization, mun=municipality)
    return scrape(query)
    
def scrapeListingWithOptions(organization, municipality, optional):
    query = "{org}+{mun}+{opt}".format(org=organization, mun=municipality, opt=optional)
    return scrape(query)
    
def unpackArgs(kwargs):
    return [kwargs.get(KWARG_ORGANIZATION),
            kwargs.get(KWARG_MUNICIPALITY),
            kwargs.get(KWARG_TAG),
            kwargs.get(KWARG_TAG_ATTRS),
            kwargs.get(KWARG_OPTIONAL)]

def validateArgs(listingOrganization, listingMunicipality, tag, tagAttributes):
    if(listingOrganization == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_ORGANIZATION))
    if(listingMunicipality == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_MUNICIPALITY))
    if(tag == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_TAG))
    if(tagAttributes == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_TAG_ATTRS))

def findTargetField(soup, tag, tagAttributes):
    html = soup.find(tag, class_=tagAttributes)
    if(html == None):
        return 'N/A'
    return html.contents[0]
        
def parseResponseForTargetField(response, tag, tagAttributes):
    soup = BeautifulSoup(response.content, 'html5lib', from_encoding='utf-8')
    return findTargetField(soup, tag, tagAttributes)

def writeContentToFile(content):
    with open('batch_file.txt', 'a') as batch_file:
        batch_file.write('{content}\n'.format(content=content))
        batch_file.close()

def main(**kwargs):
    [listingOrganization,
     listingMunicipality,
     tag,
     tagAttributes,
     optionalQueryAdditions] = unpackArgs(kwargs)
    
    validateArgs(listingOrganization, listingMunicipality, tag, tagAttributes)

    if(optionalQueryAdditions == None or optionalQueryAdditions == ''):
        res = scrapeListing(listingOrganization, listingMunicipality)
    else:
        res = scrapeListingWithOptions(listingOrganization, listingMunicipality, optionalQueryAdditions)

    targetedContent = parseResponseForTargetField(res, tag, tagAttributes)    
    writeContentToFile(targetedContent)

if __name__ == '__main__':
    main(**dict(arg.split('=') for arg in sys.argv[1:]))