from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import urllib.request
import json

from urllib.request import Request, urlopen


webpage = urlopen(req).read()

app = Flask(__name__)
journalRSSMap = {'wsj': 'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
                 'hbr': 'http://feeds.hbr.org/harvardbusiness',
                 'mit': 'https://www.technologyreview.com/feed/',
                 'econ': 'https://www.economist.com/finance-and-economics/rss.xml',
                 'mck': 'https://www.mckinsey.com/insights/rss.aspx',
                 'nyt': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
                 'lat': 'https://www.latimes.com/news/rss2.0.xml',
                 'buzz': 'https://www.buzzfeed.com/index.xml',
                 'cos': 'https://www.cosmopolitan.com/rss/all.xml/',
                 'npr': 'https://feeds.npr.org/1019/feed.json',
                 'scd': 'https://www.sciencedaily.com/rss/all.xml',
                 'lsd': 'https://www.livescience.com/feeds/all',
                 'pnas': 'https://feeds.feedburner.com/ProceedingsOfTheNationalAcademyOfSciencesMedicalSciences'}

@app.route('/news/<journal>')
def getArticles(journal):
    url = journalRSSMap[journal]
    print(url)
    toReturn = []
    if journal == 'hbr':
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html")
        for entry in soup.find_all('entry'):
            toReturn.append(entry.link['href'])
    elif journal == 'npr':
        page = urllib.request.urlopen(url)
        data = json.loads(page.read())['items']
        for obj in data:
            toReturn.append(obj['url'])
    elif joirnal == 'scd':
        req = Request('https://www.sciencedaily.com/rss/all.xml', headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, features="xml")
        for item in soup.find_all('item'):
            toReturn.append(item.link.text)
    else:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features="xml")
        for item in soup.find_all('item'):
            toReturn.append(item.link.text)
    return jsonify(toReturn)

@app.route('/isa')
def isa():
    return render_template('isa.html')

@app.route('/shravya')
def shravya():
    return render_template('shravya.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
