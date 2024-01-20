""" Module to test Poll API """
#external librares
import pytest

#internal libraries
import sys
sys.path.append(".") #allows modules to be discovered
from api import Polls, Votes


def test_PollAPI_get_returndictionary():
    #arrange
    p = Polls()
    #act
    res = p.get()
    #assert
    #type check
    assert type(res) == dict
    #key check
    assert list(res.keys()) == ['pollId', 'pollName', 'question', 'options']
    

def test_VoteAPI_get_returndictionary():
    #arrange
    pollId = 1
    v = Votes()
    #act
    res = v.get(pollId)
    #assert
    #type check
    assert type(res) == dict
    #queried Id check 
    assert res['pollId'] == pollId