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
    def __init__(self):
        """ Constructor variable to have resources in memory """
        self.poll_data = []
        self.poll_data.append(open_polljson())
        
    def get(self):
        """ Just returns example json """
        # example.json is local
        # In actual program I wil run the DataSource() concrete class to connect to a data source
        # and return data = database.execute(SELECT * FROM Table_name)
        return self.poll_data[0]

    
    
class Votes(Resource):
    """ API dealing with vote data """
    
    def __init__(self):
        """ Constructor to have resources in memory """
        self.vote_data = []
        self.vote_data.append(open_polljson())
        
    def get(self,poll_id):
        """ Gets Votes for a poll by pollID: Local Version """
        # looks through the local resource 
        for d in self.vote_data:
            if d['pollId'] == int(poll_id):
                return d
            else:
                return "Not Found"
        """ Data Base Option: Fake Code for demonstration """
        # 1. Intialise database object 
        # 2. data = db.execute(WHERE pollID = poll_id)
        # 3. if data !=None return data else return 404
        
        
        
    # def post(self,pollId,optionid):
    #     self.options_data[{pollid:optionid}] #saving locally 
    #     open self.vote_data
    #     find correct poll
    #     find correct option
    #     option += 1 
        
    #     """ db case """
    #     # get the write vote table
    #     table = db.execute(WHERE pollid= pollid)
    #     # add cone count to the optiondid
    #     db.exceute(WHERE optionid= optiond increment)
    #     return 204
        
    
        
api.add_resource(Polls,'/voting')
api.add_resource(Votes,'/polls/<poll_id>')

if __name__ == '__main__':
    app.run(debug=True)