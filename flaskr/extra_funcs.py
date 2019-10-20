import random
import string
from flaskr.Assests import CookieException

def rand_code():
    '''
    This function generates a random code for a given host session 
    => join code
    '''
    code = ""

    upper = list(string.ascii_uppercase)
    nums = list(range(0,50))

    for i in range(0,2):
        code += random.choice(upper)
        code += str(random.choice(nums))

    return code

def is_host(sessions, session, user_x):
    try: 
        current_session = sessions[session]
    except KeyError: 
        raise CookieException
    return user_x == current_session["host"]
