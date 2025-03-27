from argparse import ArgumentParser
from json import load
from sys import argv
import relationships

class Person():
    """Represents a person in a family
    
    Attributes:
        name (str) : The person's name
        gender (str) : The person's gender, represented as 'f','m', or 'n'
        parents(list) : The person's parents, if known; may be empty
        spouse (Person or None): The person's spouse if applicable, None if not
    """
    
    def __init__(self):
        raise NotImplementedError
    
    def add_parent(self):
        raise NotImplementedError
    
    def set_spouse(self):
        raise NotImplementedError

    def connections(self):
        raise NotImplementedError

    def relation_to(self):
        raise NotImplementedError
