import os
import requests
from flask import Flask, render_template, redirect, request, session, url_for, escape, make_response
from flaskr.User import User
from flaskr.extra_funcs import *
from collections import deque

sessions = dict()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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
        global sessions

        name = request.form['username']
        activation_code = request.form['code']

        if activation_code in sessions:
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
        oauthUrl += '&scope=user-read-private%20&user-read-email'
        return redirect(oauthUrl,code=302)

    @app.route('/spotifyCallback', methods=['GET','POST'])
    def spotifyAuthCallback():      
        global sessions  

        code = request.args.get('code')
        tokenUrl = 'https://accounts.spotify.com/api/token'
        data = {'grant_type':'authorization_code',
                'code':code,
                'redirect_uri':'http://localhost:5000/spotifyCallback',
                'client_id':'32a33ef6be6f484aa7af70dbc0a8be74',
                'client_secret':'8c68f3903c78478ea18f9d18a79c7d13'
        }
        res = requests.post(tokenUrl,data=data)
        authorization_header = {"Authorization":"Bearer {}".format(res.json()['access_token'])}
        userInformation = requests.get('https://api.spotify.com/v1/me',headers=authorization_header)
        
        
        random_code = rand_code()
        sessions[random_code] = dict()
        sessions[random_code]["host"] = userInformation.json()["display_name"]
        
        print(userInformation.json())
        resp = make_response(render_template('host.html', random_code = random_code))
        resp.set_cookie('sessionID', random_code)
        return resp 
        
        
    
    @app.route('/join')
    def join():
        return render_template('join.html')

    return app
