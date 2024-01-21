""" A file that stores utility classes and functions to be used across project """
#external libraries
import json
import plotly.express as px
from collections import defaultdict
import os 
import sys

#custom libraries
sys.path.append(".")#allows modules to be discovered
from classes.abstract_classes import Graph


def open_polljson()-> dict:
    """ Opens and loads local example json file """ 
    location = 'D:/python_projects/techtest2_pollapi/resources/poll_example.json'
    f = open(location)
    data = json.load(f)
    return data 

def open_votejson()-> dict:
    """ Opens and loads local example json file """ 
    location = 'D:/python_projects/techtest2_pollapi/resources/vote_example.json'
    f = open(location)
    data = json.load(f)
    return data 


class HBar(Graph):
    """ Concrete class of Graph to produce horizontal bar chart """
    def etl(self,response: object) -> dict:
        """ Calculates the percentage of results """
        # Complexity O(2N)
        if type(response) != str:
            votes_dict = response.json()
        else:
            votes_dict = eval(response)
        votes_data = votes_dict = votes_dict["options"]
        
        # collecting options and calculating sum
        total = 0
        graph_data = defaultdict(list)
        for e in votes_data:
            graph_data['Options'].append(e['optionText'])
            total += e['count']
            
        # calculating percentage and collection
        for e in votes_data:
            percentage = round((e['count'] /total)*100)
            graph_data['Percentage Votes'].append(percentage)
            
        return graph_data
    
    def fig(self,graph_data: dict) -> object:
        """ Creates graph """
        x_axis = list(graph_data.keys())[1]
        y_axis = list(graph_data.keys())[0]
        fig = px.bar(graph_data,x=x_axis,y=y_axis)
        return fig

    
    def export(self,fig:object) -> None:
        """ Writes graph to HTML File to /static """
        file = 'graph.html'
        path = 'templates/'
        file_path = path+file
        fig.write_html(file_path)
        #check if html succesfully created 
        if os.path.isfile(file_path):
            return True
        else:
            return False
        
    

