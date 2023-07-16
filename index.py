from flask import Flask, render_template
import json
import urllib.request as request

app = Flask(__name__)

api_key = "be818da11c73be0dcfaf55ed686daa7d"
base_urls = [
    {"url": "https://api.themoviedb.org/3/movie/popular?api_key=" + api_key, "category": "popular"},
    {"url": "https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_key, "category": "top_rated"},
    {"url": "https://api.themoviedb.org/3/movie/upcoming?api_key=" + api_key, "category": "upcoming"}
]

@app.route("/")
def home():
    movie_data = []
    for url in base_urls:
        conn = request.urlopen(url["url"])
        response_data = conn.read()
        json_data = json.loads(response_data)
        for movie in json_data["results"]:
            movie["category"] = url["category"]
        movie_data.extend(json_data["results"])
    return render_template("home.html", data=movie_data)

if __name__ == "__main__":
    app.run(debug=True)
