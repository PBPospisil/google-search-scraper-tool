import json
import argparse
from . scraper import Scraper
from . gs_scraper import GoogleSearchScraper
from . batch_scraper import BatchScraper

def parseJson(genericArgs):
    try:
        return json.loads(genericArgs)
    except:
        raise ValueError('Invalid argument (generic-args): error parsing json')  

def unpackArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode')
    parser.add_argument('-ga', '--generic-args')
    args = parser.parse_args()

    return [args.mode, parseJson(args.generic_args)]

def main():
    [mode, genericArgs] = unpackArgs()
    match(mode):
        case 'scrape':
            Scraper.scrape(genericArgs)
        case 'gs-scrape':
            GoogleSearchScraper.scrape(genericArgs)
        case 'batch':
            BatchScraper.scrape(genericArgs)
        case _:
            raise ValueError('Invalid argument (mode): unrecognized mode value passed')

if __name__ == '__main__':
    main()