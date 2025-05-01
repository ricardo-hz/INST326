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

def parse_number(number):
    """Removes/alters non-conforming characters to create a 10 digit number.
    
    Attributes:
        number (str or int) : The phone number to be converted.
    
    Returns:
        A valid, 10 digit phone number with no special characters or letters.
    
    Raises:
        ValueError - The phone number passed does not meet requirements. For a 
            phone number to be successfully parsed, it must have at 10 or 11 
            digits (including letters). The area code, nor the extension code 
            can begin with 0 or 1. Neither code can end with 11.
        
        TypeError - The phone number passed was of the wrong type. Accepted 
            types are string and integer.
    """
    
    # Check type
    if not isinstance(number, (str | int)):
            raise TypeError
    
    # Convert integers to string
    if isinstance(number, int):
        number = str(number)
    
    for digit in number:
        # Remove non alphanumeric characters
        if not digit.isalnum():
            number = number.replace(digit, "")
        
        # Replace letters with their numberpad counterpart
        if digit.isalpha():
            number = number.replace(digit, LETTER_TO_NUMBER[digit])
    
    # Remove country code, if there is one
    if len(number) == 11 and number[0] == "1":
        number = number[1:]
    
    # Final length check
    if len(number) != 10:
        raise ValueError(f"{number} must contain 10 digits. "
                         f"It contains {len(number)}.")
    
    number = {
    "area_code" : number[0:3],
    "exchange_code" : number[3:6],
    "line_number" : number[6:]
    }
    
    # Area codes and exchange codes cannot begin with 0 or 1, they cannot end
    # with 11
    if (any([
        number["area_code"].startswith("0"),
        number["area_code"].startswith("1"),
        number["area_code"].endswith("11"),
        number["exchange_code"].startswith("0"),
        number["exchange_code"].startswith("1"),
        number["exchange_code"].endswith("11")
        ])):
        raise ValueError("Invalid Phone Number entered")
    
    return number

class PhoneNumber():
    """Represents a phone number.
    
    Attributes:
        area_code (str) : The area code of the created PhoneNumber object.
        exchange_code (str) : The exchange code of the created PhoneNumber
            object.
        line_number (str) : The line number of the created PhoneNumber object.
    """
    def __init__(self, ph_num):
        """Initializes a PhoneNumber object.    
        
        Args:
            ph_num (str or int): The phone number that should be used to 
                instantiate the PhoneNumber object.
                
        Side effects:
            Creates a PhoneNumber object in memory.
            
        Raises:
            Any exception passed by the parse_number function. See 
            parse_number() docstring for more information.
        """
        try:
            ph_num = parse_number(ph_num) 
        except:
            raise
        
        self.area_code = ph_num["area_code"]
        self.exchange_code = ph_num["exchange_code"]
        self.line_number = ph_num["line_number"]
    
    def __str__(self):
        """Informally represents a Phone Number object as a string.
        """
        # (123) 456-7890
        return(f"({self.area_code}) {self.exchange_code}-{self.line_number}")
    
    def __int__(self):
        """Represents a Phone Number object as an integer.
        """
        # 1234567890
        return(int(f"{self.area_code}{self.exchange_code}{self.line_number}"))
    
    def __repr__(self):
        """Formally represents a Phone Number object as a string (DEBUG).
        """
        # PhoneNumber('1234567890')
        return(f"PhoneNumber('{int(self)}')")
    
    
    def __lt__(self, other):
        """Overrides the less than (<) operator.
        
        Overrides the less than (<) operator to compare integer representations
            of phone numbers.
        """
        return(int(self) < int(other))

def read_numbers(path):
    """Assembles a list of names and standardized phone numbers.
    
    Args:
        path (str) : The path to the file containing names and phone numbers in
            the format name(TAB (\\t))number
    
    Returns:
        A sorted list of tuples. Each tuple is formatted as (name,number) where
            name is a string and number is a PhoneNumber object. The list is
            sorted in ascending order by number.
    
    Side effects:
        Creates a PhoneNumber object in memory.
    """
    contact_info = []
    with open(path, 'r', encoding = "UTF-8") as f:
        for line in f:
            name = line.strip().split("\t")[0]
            number = line.strip().split("\t")[1]
            try:
                number = PhoneNumber(number)
            except:
                raise
            contact_info.append((name, number))
    return sorted(contact_info, key = lambda contact: contact[1])

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
