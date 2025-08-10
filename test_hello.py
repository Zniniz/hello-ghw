import pytest
from hello import greet

def test_greeting():
    assert greet("Bob") == "Hello, Bob!"
