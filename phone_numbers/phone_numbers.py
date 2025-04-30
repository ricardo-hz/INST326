from argparse import ArgumentParser
import re
import sys


LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}


# Replace this comment with your implementation of the PhoneNumber class and
# the `read_numbers()` function.
class PhoneNumer():
    def __init__(self, ph_num):
        # If the argument is not a string or an integer, your class should 
        # raise a TypeError
        if not isinstance(ph_num, (str | int)):
            raise TypeError
        
        # If the number is not valid, it should raise a ValueError
        # If area code or the exchange code begins with 0 or 1, or ends with 1

pattern = r"""
(?x) # Extended
^
(?:\d?\s?\W?) #Checks for cc and leading parentheses
(?P<area>\d{3}) #Finds area code
\W?\s? #Checks for closed paren and space
#\W? #Checks for space
(?P<exchange>\w{3})#Checks for exchange code
\W*
(?P<line_num>\w{4})#Checks for line number
$
"""


def main(path):
    """Read data from path and print results.
    
    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.
    
    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{number}\t{name}")


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
