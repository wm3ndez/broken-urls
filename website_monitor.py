from BeautifulSoup import BeautifulSoup as bs
import httplib
import urllib2
import time
import sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('baseurl', help='Base Url')

BASE_URL = parser.parse_args().baseurl
bad_urls = []
all_urls = []
exclude_urls = []


def map_urls(url):
    try:
        page = urllib2.urlopen(url)
    except (urllib2.HTTPError,urllib2.URLError):
        bad_urls.append(url)
        return

    soup = bs(page)
    for link in soup.findAll('a'):
        href = link.get('href')
        try:
            if href.split('?')[0] in exclude_urls: continue
            if href.startswith('/'):
                if href in all_urls: continue
                all_urls.append(href)
                print link.get('href')
                map_urls( '%s%s' % ( BASE_URL, href))
        except:
            pass


#Let the fun begin
map_urls(BASE_URL)
print '*' * 15, 'BAD URLS', '*' * 10
print ''
print bad_urls
