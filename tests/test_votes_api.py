""" File to test for Votes API """
""" Module to test Poll API """
#external librares
import pytest
import requests
import json

#internal libraries
import sys
sys.path.append(".") #allows modules to be discovered


def test_Voteget_returndictionary():
    #arrange
    poll_id = '1'
    option_id = '1'
    arg = poll_id + '/'+ option_id
    #act
    data = requests.get('http://localhost:5000/votes/'+arg)
    #assert
    assert data != None
    assert type(data.json()) == dict
    assert poll_id in data.text