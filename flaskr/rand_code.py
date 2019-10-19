import random
import string

'''
This function generates a random code for a given host session 
=> join code
'''

def rand_code():
    code = ""

    upper = list(string.ascii_uppercase)
    nums = list(range(0,50))

    for i in range(0,2):
        code += random.choice(upper)
        code += str(random.choice(nums))

    return code