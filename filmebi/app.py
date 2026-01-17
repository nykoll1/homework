from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.movies_db
movies_collection = db.movies

@app.route("/")
def index():
    movies = list(movies_collection.find())
    total_movies = movies_collection.count_documents({})
    total_duration = 0
    for movie in movies:
        total_duration += movie["duration"]
    average_duration = total_duration / total_movies

    return render_template(
        "index.html",
        movies=movies,
        total_movies=total_movies,
        average_duration=round(average_duration, 2)
    )
if __name__ == "__main__":
    app.run(debug=True)