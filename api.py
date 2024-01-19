# external modules
from flask import Flask
from flask_restful import Resource, Api
from abc import ABC


#custom modules
import sys
sys.path.append(".") #allows modules to be discovered
from classes.utility import open_polljson, open_votejson

app = Flask("API",template_folder="templates")
api = Api(app)

class Polls(Resource):
    """ API dealing with poll data """
    def get(self):
        """ Just returns example json """
        # example.json is local
        # In actual program I wil run the DataSource() concrete class to connect to a data sauce
        res = open_polljson()
        return res
    
    
class Votes(Resource):
    """ API dealing with vote data """
    def get(self,pollId=1):
        res = open_votejson()
        return res
        
    
api.add_resource(Polls,'/voting')
api.add_resource(Votes,'/confirmation')

if __name__ == '__main__':
    app.run(debug=True)