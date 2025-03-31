from argparse import ArgumentParser
import re
import sys


# replace this comment with your implementation of the Address class
# and read_addresses() function. Uncomment the __repr__() method below
# and include it in your Address class.
class Address():
    pattern = r"(^\S+) (\D+), (\D+) ([A-Z]{2}) (\d{5})" # Add names for grouping??
    def __init__(self, address):
        match = re.search(Address.pattern, address)
        if match:
            #self.address = address
            self.house_number = match.group(1)
            self.street = match.group(2)
            self.city = match.group(3)
            self.zip = match.group(4)
        else:
            raise ValueError("The string could not be parsed")

    # def __repr__(self):
    #     """Return a formal representation of the Address object."""
    #     return (
    #         f"address:      {self.address}\n"
    #         f"house number: {self.house_number}\n"
    #         f"street:       {self.street}\n"
    #         f"city:         {self.city}\n"
    #         f"state:        {self.state}\n"
    #         f"zip:          {self.zip}"
    #     )


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
