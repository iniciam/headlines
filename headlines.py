import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEED = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://rss.iol.io/iol/all-content-feed'}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEED:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEED[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
