import urllib2
from urlparse import urlparse
import tldextract
from bs4 import BeautifulSoup


def element_picker(url):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    urlchecker = urlparse(url)
    print urlchecker
    site = tldextract.extract(url)
    # print site
    if site.domain != "":
        python_dict = {"title": "", "url": "", "feature_image": "", "description": "", "categories": [], "topic": [], "keywords": [], "sub_categories": []}
        response = urllib2.urlopen(req)
        source = response.read()
        soup = BeautifulSoup(source, 'html.parser')
        for meta in soup.find_all('meta'):
            # print meta
            if 'category' == meta.get('property'):
                python_dict["categories"].append(str(meta.get('content')))
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
        print python_dict
        print "\n\n\n\n"

if __name__ == "__main__":
    # element_picker("http://www.indiatimes.com/sports/sania-mirza-slams-journo-over-his-personal-questions-says-being-no-1-is-also-settling-down-258334.html")
    # element_picker("http://sports.ndtv.com/cricket/news/260823-cricket-live-score-england-vs-pakistan-1st-test-day-1")
    # element_picker("https://scoopwhoop.com/India-Begins-Operation-Sankat-Mochan-To-Rescue-Over-300-Stranded-In-South-Sudan/")
    url_list = ["http://www.ndtv.com/delhi-news/3-found-guilty-of-killing-call-centre-executive-jigisha-ghosh-1431391?pfrom=home-lateststories", "http://sports.ndtv.com/cricket/news/260823-cricket-live-score-england-vs-pakistan-1st-test-day-1", "http://www.ndtv.com/india-news/arunachal-chief-minister-nabam-tuki-asked-to-prove-majority-on-saturday-sources-1431416?pfrom=home-lateststories", "http://goodtimes.ndtv.com/features/6-easy-exercises-to-do-before-getting-out-of-bed-1429001?",
                "http://profit.ndtv.com/news/industries/article-investors-keen-on-defence-sector-after-fdi-easing-nirmala-sitharaman-1431479", "http://www.ndtv.com/india-news/legally-i-am-chief-minister-of-arunachal-pradesh-kalikho-pul-1431469",
                "http://sports.ndtv.com/west-indies-vs-india-2016/news/260819-india-in-west-indies-anil-kumble-understands-bowlers-psyche-says-ravichandran-ashwin", "http://www.ndtv.com/india-news/at-180-km-hr-spanish-made-talgo-train-is-now-indias-fastest-now-1431378?trendingnow", "http://www.ndtv.com/health/being-overweight-obese-cuts-lifespan-by-one-to-10-years-study-1431388", "http://movies.ndtv.com/bollywood/hrithik-roshan-taken-aback-by-mohenjo-daro-co-star-poojas-courage-1431372?utm_source=taboola"]
    for item in url_list:
        element_picker(item)
        print "\n\n\n\n"
