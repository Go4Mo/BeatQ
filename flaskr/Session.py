from flaskr.extra_funcs import *
from collections import deque
'''
Class creates a session instance
'''

class Session: 

    def __init__(self, name, host):
        self.host = host
        
        # create unique code for the session
        # this identifier will enable users to join 
        # this session
        self.identifier = rand_code()  
        self.name = name # session name 
        self.songs = deque()

    def enq(self, request):
        deque.append(request)
    
    def deq(self):
        return deque.popleft()
        


    