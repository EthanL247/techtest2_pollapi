# external modules
from flask import Flask
from flask_restful import Resource, Api
from abc import ABC


#custom modules
import sys
sys.path.append(".") #allows modules to be discovered
from classes.utility import open_polljson

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
        """ In actual program I will do this
            1. Create concrete class of DataSource eg PostG = DataSource(POLL Table)
            2. PostG.Connect() to connec to database
            3. Data = PostG. Search(I.ID) to get poll from poll id within database
            4. PostG.Close() to close database 
        """
        return self.poll_data[0]

    
    
class Votes(Resource):
    """ API dealing with vote data """
    
    def __init__(self):
        """ Constructor to have resources in memory """
        self.vote_data = []
        self.vote_data.append(open_polljson())
        
    def get(self,poll_id,option_id=None):
        """ Gets Votes for a poll by pollID: Local Version """
        # looks through the local resource 
        # Complexity: O(N) 
        for d in self.vote_data:
            if d['pollId'] == int(poll_id):
                return d
            else:
                continue
        # return error if not found
        """ In actual program I will do this
            1. Create concrete class of DataSource eg PostG = DataSource(VOTE Table)
            2. PostG.Connect() to connect to database
            3. Data = PostG.Search(I.ID) to get poll from poll id within database
            4. PostG.Close() to close database 
        """
        return 404

        
        
    def post(self,poll_id,option_id):
        """ Posts poll_id and option_id to update votes: local version"""
        # Complexity: O(2N) 
        for d in self.vote_data:
            if d['pollId'] == int(poll_id):
                poll = d
            else:
                continue
        
        for element in d['options']:
            if element['optionId'] == int(option_id):
                element['count']+=1
            else:
                continue
        
        print(self.vote_data[0]) # this is here to print out that indeed local memory POLL has been updated from POST operation
        """ In actual program I will do this
            1. Create concrete class of DataSource eg PostG = DataSource(VOTE Table)
            2. PostG.Connect() to connect to database
            3. Data = PostG.Search(I.ID) to get poll from poll id within database
            4. PostG.Close() to close database 
        """
        return 204
        
    
        
api.add_resource(Polls,'/polls')
api.add_resource(Votes,'/votes/<poll_id>/<option_id>')

if __name__ == '__main__':
    app.run(debug=True)