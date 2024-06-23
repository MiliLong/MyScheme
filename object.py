"""
Define some classes to assist.
"""
from enum import Enum

class TokenType(Enum):
    """
    Define the enumeration class.
    """
    NAME = 1
    NUMBER = 2
    LPAREN = 3
    RPAREN = 4
    OPERATOR = 5

class Token:
    """
    Define the token class.
    """    
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Node:
    """
    Define the node class.
    """ 
    def __init__(self, body):
        self.body = body
    def __getitem__(self, key):
        return self.body[key]
    def __len__(self):
        return len(self.body)
    
class Function(Node):
    """
    Define the function class.
    """  
    def __init__(self, args, body):
        super().__init__(body)
        self.args = args