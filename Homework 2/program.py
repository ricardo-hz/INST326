from argparse import ArgumentParser
from json import load
from sys import argv
from relationships import relationships

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
        """Builds a dictionary representing connections between Person objects.
        
        Builds a dictionary in which each key is a Person object related to the 
        current instance (self) through a combination of parent and/or spouse 
        connections. The corresponding is a string that represents the path of
        connections from self to that particular Person instance.
        """
        # Create a dict of connections (cdict) where self is a key with an empty string as its value
        cdict = {
            self : ''
        }
        
        # Create a spouse connection list
        person_queue = [self]
        
        # While the queue is empty
        while not person_queue:
            # Take the first Person object off the queue
            person = person_queue.pop(0)
            # Look up the path from self to person in dict
            personpath = cdict[person.name]
            # For each of person's parents
            for parent in person.parents:
                if parent not in cdict:
                    # The path to the parent is personpath plus a "P" at the 
                    # end; add the parent as a new key in cdict with the path 
                    # to the parent as the corresponding value
                    cdict[parent] = f"{personpath}P"
                    # Add the parent to the end of the queue
                    person_queue.append(parent)
            # If the value of personpath doesn’t contain "S" AND person has a 
            # spouse AND person's spouse isn’t in cdict:
            if ('S' not in personpath and person.spouse and person.spouse not in cdict):
                cdict[person] = f"{personpath}S"#??????
                # Add the spouse to the end of the queue
                person_queue.append(person)
        return cdict

    def relation_to(self, person):
        """Determines the relation between self and a Person object
        
        Attributes:
            person (Person) : The other Person object to check for a
                relationship from.
        
        Returns:
            None : self and person are not related.
            'distant relative' (str) : self and other person are related, but
                there is no kinship term in relationships.relationships.
            kinship (str) : self and other person are related and a kinship
                term exists in relationships.relationships.
            """
        # Determine the relationship between self and the other person
        sdict = self.connections()
        pdict = person.connections()
        # Find keys shared by the two dictionaries.
        shared_connections = set(sdict) & set(pdict)
        # If no keys are shared, return none
        if not shared_connections:
            return None
        
        # Make an iterable of combined paths for each shared relative
        paths = [f"{sdict[connection]}:{pdict[connection]}" for connection
                 in shared_connections]
        
        # Find the path that contains the fewest characters, this is the 
        # combined path to the LCR.
        shortest_path = min(paths, key=len)
        
        # If the combined path to the LCR is a key in relationships.
        # relationships, use self.gender to look up the appropriate kinship 
        # term to describe how self is related to the other person; return 
        # that term
        # TODO: Check if this is a valid way to define relationships
        if shortest_path in relationships:
            kinship = relationships[shortest_path][self.gender]
            return(kinship)
        else:
            return "distant relative"
        
class Family():
    """Keeps track of all created Person instances.
    
    Attributes:
        people (dict) : A dict in which each key is the name of a person and
            each value is a corresponding Person object.
    """
    
    def __init__(self, d):
        """Does something???
        
        Attributes:
            d (dict) : A dictionary with the following keys:
                'individuals' (dict) : a dictionary where each key is the name
                    of a person and each value is that person's gender 
                    ('f', 'm', or 'n').
                'parents' (dict) : a dictionary where each key is the name of a 
                    person and each value is a list of the names of the person's
                    parents. Every name in 'parents' is also found in 
                    'individuals'.
                'couples' (list) : a list of lists; each inner list contains two
                    names. These two people are married to each other. Every 
                    name in 'couples' is also found in 'individuals'.

        """
        
        self.people = {
            
        }
        
        # For each person in the 'individuals' key, create an instance of Person
        # with the name and gender of this person, and add the name and instance
        # of Person to self.people
        for individual in d["individuals"]:
            name = individual
            gender = individual[name]
            person = Person(name,gender)
            self.people[name] = person
        
        # For each person in the "parents" key:
        
         
        raise NotImplementedError
    
    def relation(self):
        raise NotImplementedError
    