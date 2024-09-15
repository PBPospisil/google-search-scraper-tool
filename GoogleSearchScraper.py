#!/usr/bin/env python3

import sys
import Scraper
from services import unpackArgs, validateArgs
from constants import URL_PREFIX, ADDRESS_PATTERN_CALGARY

def composeUrl(query):
    return "{url_prefix}{query}".format(url_prefix=URL_PREFIX, query=query)
    
def buildQuery(listingOrganization, listingMunicipality, optionalQueryAdditions):
    if(optionalQueryAdditions == None or optionalQueryAdditions == ''):
        return "{org}+{mun}".format(org=listingOrganization, mun=listingMunicipality)
    else:
        return "{org}+{mun}+{opt}".format(org=listingOrganization,
                                          mun=listingMunicipality,
                                          opt=optionalQueryAdditions)

def scrape(**kwargs):
    [listingOrganization,
     listingMunicipality,
     tag,
     tagAttributes,
     optionalQueryAdditions] = unpackArgs(kwargs)
    
    validateArgs(listingOrganization, listingMunicipality, tag, tagAttributes)

    url = composeUrl(buildQuery(listingOrganization, listingMunicipality, optionalQueryAdditions))
    Scraper.scrape(url, tag, tagAttributes, ADDRESS_PATTERN_CALGARY)

if __name__ == '__main__':
    scrape(**dict(arg.split('=') for arg in sys.argv[1:]))