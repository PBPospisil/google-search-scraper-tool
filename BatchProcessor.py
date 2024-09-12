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
            GoogleSearchScraper.main(org=content[0],
                                     mun=content[1],
                                     tag=content[2],
                                     tag_attrs=content[3],
                                     opt=content[4])
        fp.close()

if __name__ == '__main__':
    main(sys.argv[1])