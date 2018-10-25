import unittest 

# thought I should have this to grab all the functions and variables from pyflix 
# to use for testing
from pyflix import *

class MoviesTest(unittest.TestCase):
   
    # hw test files had variables with stuff assigned from a variable (beatles_lst)
    # and then used the variable for tests
    
    # goal is to test the convert_list_dict function and see if 
    # it actually generates a dictionary with the correct keys
    
    
    def test_list_dict_keys(self):
        sampleDict = convert_list_dict(["batman","www.fakeurl.com","10","90","2018","action"])
        # would you need to sort both lists of keys to make sure things line up?
        self.assertEqual(sorted(sampleDict.keys()), sorted(["title","url","imdbRating","duration","year","type"]))
        
        # or should I do (looks super messy, but no local variable stuff going on)
        #self.assertEqual(sorted(convert_list_dict(["batman","www.fakeurl.com","10","90","2018","action"]).keys()), sorted(["title","url","imdbRating","duration","year","type"]))
    
    
    #practice writing setup and teardown stuff
    def setUp(self):
        with open("out.txt", "r") as f:
            self.out = f.read()
    
    def tearDown(self):
        self.out.dispose()
        self.out = None
