#!/usr/bin/env python3

import sys
import GoogleSearchScraper
from tqdm import tqdm
import json

def parseJsonParamSet(paramSet):
    try:
        return json.loads(paramSet)
    except:
        raise ValueError("Invalid batch params: error parsing json")

def main(*args):
    with open(args[0], 'r') as fp:
        contents = fp.readlines()
        numberOfLines = len(contents)
        print('\n')
        for line in tqdm(contents, total=numberOfLines, desc ='Batch progress'):
            content = parseJsonParamSet(line.rstrip('\n'))
            GoogleSearchScraper.scrape(org=content['org'],
                                       mun=content['mun'],
                                       tag=content['tag'],
                                       attrs=content['attrs'],
                                       pattern=content['pattern'],
                                       opt=content['opt'])
        fp.close()

if __name__ == '__main__':
    main(sys.argv[1])