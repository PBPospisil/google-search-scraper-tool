#!/usr/bin/env python3

from .. scraper import Scraper
from .. constants import (URL_PREFIX,
                          KWARG_KEYWORDS,
                          KWARG_TAG,
                          KWARG_TARGET_ATTRS,
                          KWARG_PATTERN,
                          KWARG_RESULTS_FILE)

def unpackArgs(kwargs):
    return [kwargs.get(KWARG_KEYWORDS),
            kwargs.get(KWARG_TAG),
            kwargs.get(KWARG_TARGET_ATTRS),
            kwargs.get(KWARG_PATTERN),
            kwargs.get(KWARG_RESULTS_FILE)]

def validateArgs(queryKeywords):
    if(queryKeywords is None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_KEYWORDS))
    
def composeUrl(query):
    return "{url_prefix}{query}".format(url_prefix=URL_PREFIX, query=query)

def buildQuery(queryKeywords):
    return queryKeywords.replace(' ', '+')

def scrape(**kwargs):
    [queryKeywords,
     targetTag,
     targetAttributes,
     altPattern,
     resultsFilename] = unpackArgs(kwargs)
    
    validateArgs(queryKeywords)

    Scraper.scrape({ 'url': composeUrl(buildQuery(queryKeywords)),
                     'tag': targetTag, 
                     'attrs': targetAttributes, 
                     'pattern': altPattern, 
                     'results': resultsFilename })