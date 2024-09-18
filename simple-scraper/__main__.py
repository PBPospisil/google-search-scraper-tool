import json
import argparse
from . scraper import Scraper
from . gs_scraper import GoogleSearchScraper
from . batch_scraper import BatchScraper

def parseJson(args):
    try:
        return json.loads(args)
    except:
        raise ValueError('Invalid argument (args): error parsing json')  

def unpackArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode')
    parser.add_argument('-a', '--args')
    args = parser.parse_args()
    return [args.mode, parseJson(args.args)]

def main():
    [mode, args] = unpackArgs()
    match(mode):
        case 'scrape':
            Scraper.scrape(args)
        case 'gs-scrape':
            GoogleSearchScraper.scrape(args)
        case 'batch':
            BatchScraper.scrape(args)
        case _:
            raise ValueError('Invalid argument (mode): unrecognized mode value passed')

if __name__ == '__main__':
    main()