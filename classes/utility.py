""" A file that stores utility classes and functions to be used across project """
#external libraries
import json
import plotly.express as px

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
    total =  sum(list(votes_data.values()))
    graph_data = {}
    for option in votes_data:
        graph_data[option] = round((votes_data[option]/total)*100)
    return graph_data
    
    
graph_data={
    "option1": 80,
    "option2": 10,
    "option3":10
}

def display_graph(graph_data: dict) -> None:
    fig - px.bar(graph_data)
    plt.show()
    
display_graph


    