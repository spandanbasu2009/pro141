from flask import Flask,jsonify
import csv
from storage import articles,liked_articles,did_not_like_articles
from demofil import output
from contentfil import get_recommendations
import itertools

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True)
 


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

@app.route("/unwatched-articles",methods = ["POST"])
def unwatched_articles():
    article = articles[0]
    articles = articles[1:]
    not_watched.append(article)
    return jsonify({
        "status":"success"
    })

@app.route("/popular-articles")
def popular_article():
    popular_articles = []
    for i in output:
        article = {
            "title":i[10]
        }
        popular_articles.append(article)
    return jsonify({
        "data":popular_articles,
        "status":"success"
    })

@app.route("/recommended-articles")
def recommended_article():
    recommended_articles = []
    for i in liked_articles:
        output = get_recommendations(i[10])
        for j in output:
            recommended_articles.append(j)
    recommended_articles.sort()
    recommended_articles = list(recommended_articles for recommended_articles,_ in itertools.groupby(recommended_articles))
    article_data = []
    for h in recommended_articles:
        data = {
            "title":h[10]
        }
        article_data.append(data)
    return jsonify({
        "data":article_data,
        "status":"success"
    })
