import os
import requests
from flask import Flask, render_template, redirect, request, session, url_for, escape
from flaskr.User import User
from flaskr.extra_funcs import *
from collections import deque

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.SECRET_KEY = rand_code()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
 
    @app.route('/')
    def index():
        return render_template('home.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/join_data', methods=["POST"])
    def join_data():
        print("Hello world")
        name = request.form['username']
        activation_code = request.form['code']
        
        if validate_code(activation_code):
            new_user = User(False, name, session)
            return render_template('home.html')
        else:
            return render_template('join.html', invalid = True)

    
    @app.route('/spotifyAuth')
    def spotifyAuth():
        oauthUrl = 'https://accounts.spotify.com/authorize'
        oauthUrl += '?response_type=code'
        oauthUrl += '&client_id=32a33ef6be6f484aa7af70dbc0a8be74'
        oauthUrl += '&redirect_uri=http://localhost:5000/spotifyCallback'
        return redirect(oauthUrl,code=302)

    @app.route('/spotifyCallback', methods=['GET','POST'])
    def spotifyAuthCallback():
        code = request.args.get('code')
        tokenUrl = 'https://accounts.spotify.com/api/token'
        data = {'grant_type':'authorization_code',
                'code':code,
                'redirect_uri':'http://localhost:5000/spotifyCallback',
                'client_id':'32a33ef6be6f484aa7af70dbc0a8be74',
                'client_secret':'8c68f3903c78478ea18f9d18a79c7d13'
        }
        random_code = rand_code()
        Session[random_code] = dict()
        Session[random_code]["host"] = "temp"
        Session[random_code]["users"] = dict()
        Session[random_code]["songs"] = deque()
        res = requests.post(tokenUrl,data=data)
        print(res.json())
        return render_template('host.html', random_code = random_code)
    
    @app.route('/join')
    def join():
        return render_template('join.html')

    return app
