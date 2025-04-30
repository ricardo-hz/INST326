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

def shift_numbers(number):
    #if len(number) != 10:
        #raise ValueError(f"{number} must be 10 digits long.")
    
    if isinstance(number, int):
        number = str(number)
    
    for digit in number:
        if not digit.isalnum():
            number = number.replace(digit, "")
            
        if digit.isalpha():
            number = number.replace(digit, LETTER_TO_NUMBER[digit])
    
    return {
        "area_code" : number[0:3],
        "exchange_number" : number[3:6],
        "line_number" : number[6:11]
    }

pattern = r"""(?x)
^
(?:1?\s?\W?)? #Checks for cc and leading parentheses
(?P<area>\w{3}) #Finds area code
#\W?\s? #Checks for closed paren and space
[\s\W]*
(?P<exchange>\w{2,7})#Checks for exchange code
#\W?
[\s\W]*
(?P<line_num>\w{1,5})#Checks for line number
$
"""

# Replace this comment with your implementation of the PhoneNumber class and
# the `read_numbers()` function.
class PhoneNumber():
    def __init__(self, ph_num):
        # If the argument is not a string or an integer, your class should 
        # raise a TypeError
        if not isinstance(ph_num, (str | int)):
            raise TypeError
        
        # If the number is not valid, it should raise a ValueError
        # If area code or the exchange code begins with 0 or 1, or ends with 1
        if not re.match(pattern, ph_num):
            raise ValueError ("Here 1")
        else:
            match = re.match(pattern, ph_num)
            ph_num = match.group("area") + match.group("exchange") + match.group("line_num")
            ph_num = shift_numbers(ph_num)
            
        if (any([
            ph_num["area_code"].startswith("0"),
            ph_num["area_code"].startswith("1"),
            ph_num["area_code"].endswith("11"),
            ph_num["exchange_number"].startswith("0"),
            ph_num["exchange_number"].startswith("1"),
            ph_num["exchange_number"].endswith("11")
            ])):
            raise ValueError("Here 2")
        
        self.area_code = ph_num["area_code"]
        self.exchange_code = ph_num["exchange_number"]
        self.line_number = ph_num["line_number"]
        
    def __repr__(self):
        return(f"{self.area_code}{self.exchange_code}{self.line_number}")
    
    def __int__(self):
        return(int(self.__repr__()))
    
    def __lt__(self, other):
        return(int(self) < int(other))
    
n1 = PhoneNumber("(234) 567-8901")
n2 = PhoneNumber("1-800-POTATO-3")
n3 = PhoneNumber("703*242*0731")

print(n1 < n2)
print(n2 < n3)
exit()
    #def __repr__():
     #   pass
    # This method needs to convert the letters to numbers
    

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
