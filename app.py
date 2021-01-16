import os
from flask import Flask, render_template, request, json, jsonify, current_app as app 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Team Edge!'

@app.route('/api/v1/movies/all', methods=['GET'])
def api_movies_all():
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_data, 'r') as jsondata:
        movies = json.load(jsondata)
    return jsonify(movies)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')