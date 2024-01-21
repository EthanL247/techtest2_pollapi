""" A file that stores utility classes and functions to be used across project """
#external libraries
import json
import plotly.express as px
from collections import defaultdict
from classes.abstract_classes import Graph

#custom libraries
import sys
sys.path.append(".")#allows modules to be discovered

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
        votes_dict = response.json()
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

    
    def output(self,fig:object) -> None:
        pass
    

# def create_graph(graph_data: dict) -> object:
#     x_axis = list(graph_data.keys())[1]
#     y_axis = list(graph_data.keys())[0]
#     return px.bar(graph_data,x=x_axis,y=y_axis)

# graph_data= defaultdict(list)
# graph_data["Options"] =['Manchester','Arsenal','Liverpool']
# graph_data['Percentage of Votes'] = [20,40,40]

# fig = px.bar(graph_data,x=list(graph_data.keys())[1],y=list(graph_data.keys())[0])
# fig.show()