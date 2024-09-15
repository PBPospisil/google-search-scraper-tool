#!/usr/bin/env python3

import sys
import GoogleSearchScraper
from tqdm import tqdm

def main(sourceFileName):
    with open(sourceFileName, 'r') as fp:
        contents = fp.readlines()
        numberOfLines = len(contents)
        print('\n')
        for line in tqdm(contents, total=numberOfLines, desc ='Batch Progress'):
            content = line.rstrip('\n').split(',')
            GoogleSearchScraper.scrape(org=content[0],
                                     mun=content[1],
                                     attrs=content[2],
                                     opt=content[3])
        fp.close()

if __name__ == '__main__':
    main(sys.argv[1])