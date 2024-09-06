from flask import Flask, render_template
from dotenv import load_dotenv
import urllib.request, json

import os
load_dotenv()

app = Flask(__name__)

@app.route("/movies")
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.getenv("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("movies.html", movies = dict["results"])

@app.route("/movies/json")
def get_movies_json():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.getenv("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    # reinitializing movies into an empty array

    movies = []

    # iterating over the obj received from server, going to the ["results"] array
    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"]
        }

        movies.append(movie)

    with open("data/data.json", "w", encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii="False", indent=4)


    # modifying result to make it into an obj with a nested array
    return {"results": movies}

if __name__ == '__main__':
    app.run(debug=True)