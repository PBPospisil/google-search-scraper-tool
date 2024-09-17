#!/usr/bin/env python3

import sys
from .. gs_scraper import GoogleSearchScraper
from tqdm import tqdm
import json
from .. constants import ARG_BATCH_FILENAME, KWARG_RESULTS_FILE

def unpackArgs(args):
    return [args.get(ARG_BATCH_FILENAME), args.get(KWARG_RESULTS_FILE)]

def validateArgs(batchArgsFilename, resultsFilename):
    if(batchArgsFilename is None or not batchArgsFilename):
        raise ValueError("Invalid argument ({arg})".format(arg=ARG_BATCH_FILENAME))
    if(resultsFilename is None or not resultsFilename):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_RESULTS_FILE))

def parseJsonParamSet(paramSet):
    try:
        return json.loads(paramSet)
    except:
        raise ValueError("Invalid batch params: error parsing json")

def scrapeFromBatchArgs(fileContents, numberOfLines, resultsFilename):
    for line in tqdm(fileContents, total=numberOfLines, desc='Batch progress'):
        content = parseJsonParamSet(line.rstrip('\n'))
        GoogleSearchScraper.scrape(org=content['org'],
                                    mun=content['mun'],
                                    tag=content['tag'],
                                    attrs=content['attrs'],
                                    pattern=content['pattern'],
                                    results=resultsFilename,
                                    opt=content['opt'])

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