""" A file that stores utility classes and functions to be used across project """
#external libraries
import json
import plotly.express as px
from collections import defaultdict

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


def percent_calc(response_text: object) -> dict:
    """ Calculates percentage from vote returns dict: option:%count """
    votes_dict = json.loads(response_text)
    votes_data = votes_dict["data"]
    
    graph_data = defaultdict(list)
    graph_data["Options"] = list(votes_data.keys())
    total =  sum(list(votes_data.values()))
    for option in votes_data:
        int_percentage = round((votes_data[option]/total)*100)
        graph_data["Percentage of Votes"].append(int_percentage)
    
    return graph_data


# def create_graph(graph_data: dict) -> object:
#     x_axis = list(graph_data.keys())[1]
#     y_axis = list(graph_data.keys())[0]
#     return px.bar(graph_data,x=x_axis,y=y_axis)

# graph_data= defaultdict(list)
# graph_data["Options"] =['Manchester','Arsenal','Liverpool']
# graph_data['Percentage of Votes'] = [20,40,40]

# fig = px.bar(graph_data,x=list(graph_data.keys())[1],y=list(graph_data.keys())[0])
# fig.show()
    