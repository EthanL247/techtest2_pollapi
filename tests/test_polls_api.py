""" Module to test Poll API """
#external librares
import pytest

#internal libraries
import sys
sys.path.append(".") #allows modules to be discovered
from api import Polls


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
