from argparse import ArgumentParser
import re
import sys

class Address():
    """Represents an address
    
    Attributes:
        address (str) : The entire address as a string. The string should not
            contain leading or trailing spaces.
        house_number (str) : The house number of the address (e.g., 5173B).
        street (str): The street name (e.g., 63rd Ave NE).
        city (str): The city (e.g., Lake Forest Park).
        state (str): The state (e.g., WA).
        zip (str): The zip code (e.g., 98155).
    """
    pattern = r"(?P<street_number>^\S+) (?P<street_name>.+), "\
        r"(?P<city>\D+) (?P<state>[A-Z]{2}) (?P<zip>\d{5})"
        
    def __init__(self, address):
        """Initializes an address object.
        
        Args:
            address (str) : The entire address as a string with no leading or
                trailing spaces.
        
        Raises:
            ValueError : raised when an address cannot be parsed by the regular
                expression.
    
        Side effects:
            Creates an Address object in memory.
        """
        match = re.search(Address.pattern, address)
        if match:
            self.address = match.group(0)
            self.house_number = match.group("street_number")
            self.street = match.group("street_name")
            self.city = match.group("city")
            self.state = match.group("state")
            self.zip = match.group("zip")
        else:
            raise ValueError(f"{address} could not be parsed")

    def __repr__(self):
        """Return a formal representation of the Address object."""
        return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
        )


def read_addresses(path):
    """Reads addresses from a file.
    
    Args:
        path (str) : The path to a file with one address per line.
    
    Returns:
        address_list (list) : A list in which each index is an Address object
            for the corresponding address in path.
    
    Side effects:
        Creates an address object for each address in path.
    """
    with open(path, 'r', encoding="utf-8") as f:
        address_list = [Address(line) for line in f]
    return address_list


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
