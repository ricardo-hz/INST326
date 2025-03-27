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
    
    def __init__(self, name, gender):
        """Initializes a Person object.
        
        Initializes a Person object by setting the name, gender, parents, and 
        spouse attributes of the object.
        
        Attributes:
            name (str) : The name of the Person
            gender (str) : The gender of the Person represented as 'f', 'm', or
            'n'
        """
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None
    
    def add_parent(self, parent):
        """Adds a parent to the parents list of a Person object.
        
        Attributes:
            parent (Person) : The parent to be added
        """
        self.parents.append(parent)
    
    def set_spouse(self, spouse):
        """Sets the spouse attribute of a Person object.
        
        Attributes:
            spouse (Person) : The person's spouse.
        """
        self.spouse = spouse

    def connections(self):
        raise NotImplementedError

    def relation_to(self):
        raise NotImplementedError
