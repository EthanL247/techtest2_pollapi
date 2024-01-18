""" A file that stores utility classes and functions to be used across project """
#external libraries
import json

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





    