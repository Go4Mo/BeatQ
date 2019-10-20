from flaskr.extra_funcs import *
'''
User class contains data for a given
user instance
'''

class User:

    def __init__(self, is_host, name, session):
        self.is_host = is_host 
        self.name = name
        self.session = session # which session the user belongs to
        self.identifier = rand_code() # identifies a given user's session 
        self.songs = []
        self.api = None

    def set_api(self, api):
        self.api = api

    def add_song(self, song):
        self.songs.append(song)

    def __eq__(self, other):
        if not isinstance(other, User): 
            return False
        return self.identifier == other.identifier 