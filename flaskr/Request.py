from flask import jsonify
'''
Request is created whenever a user enqueues a song 
'''

class Request:

    def __init__(self, json, user):
        # iterate through the json return to build this class        
        self.user = user
    
