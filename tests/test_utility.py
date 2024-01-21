""" File for testing any utility functions """
#external librares
import pytest
import requests
import json

#internal libraries
import sys
sys.path.append(".") #allows modules to be discovered
from classes.utility import HBar


@pytest.fixture
def response() -> object:
    return requests.get('http://localhost:5000/votes/1/1')

def test_Hbar_percentage_calc_returndictionary(response):
    # act
    hbar = HBar()
    #act
    res = hbar.etl(response)
    print(res)
    #assert
    assert sorted(['Arsenal','Manchester City','Liverpool']) == sorted(res['Options'])
    assert sum(res['Percentage Votes']) == 100 

def test_HBar_fig_return_figobject(response):
    # act
    hbar = HBar()
    #act
    data = hbar.etl(response)
    fig = hbar.fig(data)
    #assert
    assert str(type(fig)) == "<class 'plotly.graph_objs._figure.Figure'>"