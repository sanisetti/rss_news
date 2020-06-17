from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)
journalRSSMap = {'wsj': 'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
                 'hbr': 'http://feeds.hbr.org/harvardbusiness',
                 'mit': 'https://www.technologyreview.com/feed/',
                 'econ': 'https://www.economist.com/finance-and-economics/rss.xml',
                 'mck': 'https://www.mckinsey.com/insights/rss.aspx'}

@app.route('/news/<journal>')
def getArticles(journal):
    url = journalRSSMap[journal]
    toReturn = []
    if journal == 'hbr':
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html")
        for entry in soup.find_all('entry'):
            toReturn.append(entry.link['href'])
    else:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "xml")
        for item in soup.find_all('item'):
            toReturn.append(item.link.text)
    return jsonify(toReturn);

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
