from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["movies_db"]
movies_collection = db["movies"]

movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Sci-Fi", "duration": 148},
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Action", "duration": 136},
    {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi", "duration": 169},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime", "duration": 175},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime", "duration": 154},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action", "duration": 152},
    {"title": "Fight Club", "year": 1999, "rating": 8.8, "genre": "Drama", "duration": 139},
    {"title": "Forrest Gump", "year": 1994, "rating": 8.8, "genre": "Drama", "duration": 142},
    {"title": "The Shawshank Redemption", "year": 1994, "rating": 9.3, "genre": "Drama", "duration": 142},
    {"title": "The Prestige", "year": 2006, "rating": 8.5, "genre": "Drama", "duration": 130},
    {"title": "Avatar", "year": 2009, "rating": 7.8, "genre": "Sci-Fi", "duration": 162},
    {"title": "Whiplash", "year": 2014, "rating": 8.5, "genre": "Drama", "duration": 106},
    {"title": "Joker", "year": 2019, "rating": 8.4, "genre": "Drama", "duration": 122},
    {"title": "Parasite", "year": 2019, "rating": 8.5, "genre": "Thriller", "duration": 132},
    {"title": "The Wolf of Wall Street", "year": 2013, "rating": 8.2, "genre": "Biography", "duration": 180},
    {"title": "Mad Max: Fury Road", "year": 2015, "rating": 8.1, "genre": "Action", "duration": 120},
    {"title": "Django Unchained", "year": 2012, "rating": 8.4, "genre": "Western", "duration": 165}
]
movies_collection.insert_many(movies)
