#!/usr/bin/env python3

import sys
from .. gs_scraper import GoogleSearchScraper
from tqdm import tqdm
import json
from .. constants import BATCH_ARG_FILENAME, RESULTS_FILENAME

def unpackArgs(args):
    return [args.get(BATCH_ARG_FILENAME), args.get(RESULTS_FILENAME)]

def validateArgs(batchArgsFilename, resultsFilename):
    if(batchArgsFilename is None or not batchArgsFilename):
        raise ValueError("Invalid argument ({arg})".format(arg=BATCH_ARG_FILENAME))
    if(resultsFilename is None or not resultsFilename):
        raise ValueError("Invalid argument ({arg})".format(arg=RESULTS_FILENAME))

def parseJsonParamSet(paramSet):
    try:
        return json.loads(paramSet)
    except:
        raise ValueError("Invalid batch params: error parsing json")

def scrapeFromBatchArgs(fileContents, numberOfLines, resultsFilename):
    for line in tqdm(fileContents, total=numberOfLines, desc='Batch progress'):
        content = parseJsonParamSet(line.rstrip('\n'))
        content['results'] = resultsFilename
        GoogleSearchScraper.scrape(content)

def readFileContentsAndScrape(batchArgsFilename, resultsFilename):
    with open(batchArgsFilename, 'r') as fp:
        contents = fp.readlines()
        numberOfLines = len(contents)
        print('\n')
        scrapeFromBatchArgs(contents, numberOfLines, resultsFilename)
        fp.close()

def scrape(batchArgs):
    [batchArgsFilename, resultsFilename] = unpackArgs(batchArgs)
    print(batchArgsFilename, resultsFilename)
    validateArgs(batchArgsFilename, resultsFilename)
    readFileContentsAndScrape(batchArgsFilename, resultsFilename)