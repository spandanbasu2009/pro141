from flask import Flask,jsonify
import csv

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True)
 
articles = []

with open("shared_articles.csv") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    articles = data[1:]

liked_articles = []
did_not_like_articles = []
not_watched = []

@app.route("/get-articles")
def get_articles():
    return jsonify({
      "data": articles[0],
      "status":"success"
    })

@app.route("/liked-articles",methods = ["POST"])
def liked_article():
    article = articles[0]
    articles = articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    })

@app.route("/unliked-articles",methods = ["POST"])
def unliked_article():
    article = articles[0]
    articles = articles[1:]
    did_not_like_articles.append(article)
    return jsonify({
        "status":"success"
    })

@app.route("/unwatched-article",methods = ["POST"])
def unwatched_articles():
    article = articles[0]
    articles = articles[1:]
    not_watched.append(article)
    return jsonify({
        "status":"success"
    })