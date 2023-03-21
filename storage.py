import csv

articles = []

with open("shared_articles.csv") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    articles = data[1:]

liked_articles = []
did_not_like_articles = []