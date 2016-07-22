import urllib2
from urlparse import urlparse
import tldextract
from bs4 import BeautifulSoup


def element_picker(url):
    try:
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
        urlchecker = urlparse(url)
        site = tldextract.extract(url)
        if site.domain != "":
            python_dict = {"title": "", "url": "", "feature_image": "", "description": "", "category": [], "keywords": [], "interest": []}
            response = urllib2.urlopen(req)
            source = response.read()
            soup = BeautifulSoup(source, 'html.parser')
            for meta in soup.find_all('meta'):
                if 'category' == meta.get('property') or 'category' == meta.get('name') or 'vr:category' == meta.get('property') or 'article:section' == meta.get('property') or 'channel' == meta.get('name'):
                    python_dict["category"].append((str(meta.get('content').encode('utf-8'))).lower())
                if 'og:title' == meta.get('property'):
                    python_dict["title"] = str(meta.get('content').encode('utf-8'))
                if 'og:url' == meta.get('property'):
                    python_dict["url"] = str(meta.get('content').encode('utf-8'))
                if 'og:image' == meta.get('property'):
                    python_dict["feature_image"] = str(meta.get('content').encode('utf-8'))
                if 'description' == meta.get('property') or 'og:description' == meta.get('property') or 'description' == meta.get('name') or 'og:description' == meta.get('name'):
                    python_dict["description"] = str(meta.get('content').encode('utf-8'))
                if 'keywords' == meta.get('property') or 'keywords' == meta.get('itemprop') or 'keywords' == meta.get('name'):
                    python_dict["keywords"].append(str(meta.get('content').encode('utf-8')))
                elif 'article:tag' == meta.get('property'):
                    python_dict["keywords"].append(str(meta.get('content').encode('utf-8')))
            return python_dict
    except Exception as e:
        print e
        return python_dict