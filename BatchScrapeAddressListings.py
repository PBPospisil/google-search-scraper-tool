#!/usr/bin/env python3

import LocalListingScraper
import time
from tqdm import tqdm

def main():
    with open('address-queries-batch.txt', 'r') as fp:
        contents = fp.readlines()
        numberOfLines = len(contents)
        print('\n')
        for line in tqdm(contents, total=numberOfLines, desc ='Batch Progress'):
            content = line.rstrip('\n').split(',')
            LocalListingScraper.main(org=content[0],
                                     mun=content[1],
                                     tag=content[2],
                                     tag_attrs=content[3],
                                     opt=content[4])
        fp.close()

if __name__ == '__main__':
    main()