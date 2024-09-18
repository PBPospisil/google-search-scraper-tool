#!/usr/bin/env python3

from .. scraper import Scraper
from .. constants import (URL_PREFIX,
                          KEYWORDS,
                          TARGET_TAG,
                          TARGET_ATTRS,
                          TARGET_PATTERN,
                          RESULTS_FILENAME)

def unpackArgs(kwargs):
    return [kwargs.get(KEYWORDS),
            kwargs.get(TARGET_TAG),
            kwargs.get(TARGET_ATTRS),
            kwargs.get(TARGET_PATTERN),
            kwargs.get(RESULTS_FILENAME)]

def validateArgs(queryKeywords):
    if(queryKeywords is None or not queryKeywords):
        raise ValueError("Invalid argument ({arg})".format(arg=KEYWORDS))
    
def composeUrl(query):
    return "{url_prefix}{query}".format(url_prefix=URL_PREFIX, query=query)

def buildQuery(queryKeywords):
    return queryKeywords.replace(' ', '+')

def scrape(args):
    [queryKeywords,
     targetTag,
     targetAttributes,
     altPattern,
     resultsFilename] = unpackArgs(args)

    validateArgs(queryKeywords)

    Scraper.scrape({ 'url': composeUrl(buildQuery(queryKeywords)),
                     'tag': targetTag, 
                     'attrs': targetAttributes, 
                     'pattern': altPattern, 
                     'results': resultsFilename })