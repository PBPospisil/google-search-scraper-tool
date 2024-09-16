#!/usr/bin/env python3

import sys
import Scraper
from constants import (URL_PREFIX,
                       KWARG_ORGANIZATION,
                       KWARG_MUNICIPALITY,
                       KWARG_TAG,
                       KWARG_TARGET_ATTRS,
                       KWARG_PATTERN,
                       KWARG_OPTIONAL)

def unpackArgs(kwargs):
    return [kwargs.get(KWARG_ORGANIZATION),
            kwargs.get(KWARG_MUNICIPALITY),
            kwargs.get(KWARG_TAG),
            kwargs.get(KWARG_TARGET_ATTRS),
            kwargs.get(KWARG_PATTERN),
            kwargs.get(KWARG_OPTIONAL)]

def validateArgs(listingOrganization, listingMunicipality):
    if(listingOrganization is None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_ORGANIZATION))
    if(listingMunicipality is None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_MUNICIPALITY))
    
def composeUrl(query):
    return "{url_prefix}{query}".format(url_prefix=URL_PREFIX, query=query)

def buildQuery(listingOrganization, listingMunicipality, optionalQueryAdditions=''):
    if(optionalQueryAdditions == None or optionalQueryAdditions == ''):
        return "{org}+{mun}".format(org=listingOrganization, mun=listingMunicipality)
    else:
        return "{org}+{mun}+{opt}".format(org=listingOrganization,
                                          mun=listingMunicipality,
                                          opt=optionalQueryAdditions)

def scrape(**kwargs):
    [listingOrganization,
     listingMunicipality,
     targetTag,
     targetAttributes,
     altPattern,
     optionalQueryAdditions] = unpackArgs(kwargs)
    
    validateArgs(listingOrganization, listingMunicipality)

    url = composeUrl(buildQuery(listingOrganization, listingMunicipality, optionalQueryAdditions))
    Scraper.scrape(url, targetTag, targetAttributes, altPattern)

if __name__ == '__main__':
    scrape(**dict(arg.split('=') for arg in sys.argv[1:]))