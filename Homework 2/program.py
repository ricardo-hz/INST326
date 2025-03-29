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
        
        Args:
            name (str) : The name of the Person
            gender (str) : The gender of the Person represented as 'f', 'm', or
            'n'
        
        Side effects:
            Creates a Person object
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
        
        Returns:
            cdict (dict) - A dictionary in which each key is an instance of 
                Person to whom self is related via a combination of parent 
                and/or spouse connections, and the corresponding value is a 
                string indicating a path of connections from self to that 
                instance of Person
        """
        cdict = {
            self : ''
        }
        # Person objects whose spouse parent connections we need to follow
        person_objects = [self]
        
        while person_objects:
            person = person_objects.pop(0)
            personpath = cdict[person]
            # For each of person's parents
            for parent in person.parents:
                if parent not in cdict:
                    cdict[parent] = f"{personpath}P"
                    person_objects.append(parent)
            if "S" not in personpath and person.spouse and (person.spouse not in cdict):
                cdict[person.spouse] = f"{personpath}S"
                person_objects.append(person.spouse)
        return cdict

    def relation_to(self, person):
        """Determines the relation between self and a Person object
        
        Args:
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
        return "distant relative"
        
class Family():
    """Keeps track of all created Person instances.
    
    Attributes:
        people (dict) : A dict in which each key is the name of a person and
            each value is a corresponding Person object.
    """
    
    def __init__(self, d):
        """Does something???
        
        Args:
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
        
        Side effects:
            Initializes a Family object
        """
        
        self.people = {
            
        }
        
        # For each person in the 'individuals' key, create an instance of Person
        # with the name and gender of this person, and add the name and instance
        # of Person to self.people
        for individual in d["individuals"]:
            name = individual
            gender = d["individuals"][name]
            person = Person(name,gender)
            self.people[name] = person
        
        # For each person in the "parents" key:
        for person in d["parents"]:
                # Look up the Person object corresponding to parent
                p = self.people[person]
                for parent in d["parents"][person]:
                    parent = self.people[parent]
                    p.add_parent(parent)
                    
        for couple in d["couples"]:
            husb = self.people[couple[0]]
            wife = self.people[couple[1]]
            husb.set_spouse(wife)
            wife.set_spouse(husb)
    
    def relation(self, person1, person2): #This method doesn't work, not passed Person objects???
        """Returns the relationship between two Person objects
        
        Args:
            person1 (Person) : The person to check for relationships of
            person2 (Person) : The person to check for relations to person1
        
        Returns:
            None if no kinship found, else a string expressing kinship
        """
        return self.people[person1].relation_to(self.people[person2])

def main(path, person_name1, person_name2):
    """Implement this docstring later
    """
    with open(path, 'r', encoding = "UTF-8") as f:
        familydata = load(f) #Load json
        family = Family(familydata)
        relation = family.relation(person_name1, person_name2)
        print(f"{person_name1} is not related to {person_name2}" if not relation
               else f"{person_name1} is {person_name2}'s {relation}")

def parse_args(args):
    """Implement this docstring later
    """
    arg_parser = ArgumentParser()
    arg_parser.add_argument("filepath", help = "A help message")
    arg_parser.add_argument("name1", help = "A help message")
    arg_parser.add_argument("name2", help = "A help message")
    
    return arg_parser.parse_args(args)
    #raise NotImplementedError

if __name__ == "__main__":
    """Implement this docstring later
    """
    #raise NotImplementedError


d = {
    "individuals" : {
        "Sarah" : "f",
        "Jacob" : "m",
        "Paul" : "n"    
    },
    "parents" : {
        "Paul" : ["Sarah", "Jacob"]
    },
    "couples" : [["Sarah", "Jacob"]]
}

p = Person("Paul","n")
s = Person("Sarah", "f")
p.add_parent(s)
family = Family(d)

p.connections()