from flask import Flask, render_template
from dotenv import load_dotenv
import urllib.request, json

import os
load_dotenv()

app = Flask(__name__)

@app.route("/movies")
def get_movies():
    print("key: " + os.getenv("TMDB_API_KEY"))
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.getenv("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("movies.html", movies = dict["results"])


if __name__ == '__main__':
    app.run(debug=True)