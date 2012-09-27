from BeautifulSoup import BeautifulSoup as bs
import httplib
import urllib2
import time
import sys
bad_urls = []
DOMAIN_BASE_URL = 'http://localhost:8000'
exclude_urls = []


def map_urls(url):
    try:
        page = urllib2.urlopen(url) # maybe, I'm going off memory
    except (urllib2.HTTPError,urllib2.URLError):
        bad_urls.append(url)
        return

    soup = bs(page)
    for link in soup.findAll('a'):
        href = link.get('href')
        try:
            if href.split('?')[0] in exclude_urls: continue
            if href.startswith('/'):
                try:
                    all_urls[href] += 1
                except KeyError:
                    all_urls[href] = 0
                    print link.get('href')
                    map_urls( '%s%s' % ( DOMAIN_BASE_URL, href))
        except:
            pass


all_urls = {}

map_urls(DOMAIN_BASE_URL)
print '*' * 15, 'BAD URLS', '*' * 10
print ''
print bad_urls
