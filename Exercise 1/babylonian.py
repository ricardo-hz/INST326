"""Use the Babylonian method to approximate the square root of a positive
number."""


from argparse import ArgumentParser
import sys


def sqrt_b(positive_number, precision = 1e-10):
    """Compute an approximation of a square root using the Babylonian method
    
    Args:
        positive_number (int or float): The number to compute the square root of
        precision (float or optional): The precision required for the
            approximate square root. Should be a float between 0 and 1.
            Default: 1e-10
    
    Returns:
        float: The approximate square root of s.
    """
    init_guess = abs(positive_number)//2 #Make initial guess about sqrt (x)
    approximation = (init_guess + (positive_number / init_guess) / 2)#Compute y
    epsilon = abs(approximation - init_guess)#Calculate |y-x|
    while(epsilon > precision): #Step 4 of algorithm
        init_guess = approximation #Step 5
        approximation = (init_guess + (positive_number / init_guess)) / 2
        epsilon = abs(approximation - init_guess)
    return approximation



def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect one required argument (a positive number whose square root the user
    wants to calculate) and one optional parameter (a precision, specified by
    the short flag -p or the long flag --precision). Both values
    are floats. The default precision is 0.0000000001 (1e-10).
    
    Args:
        arglist (list of str): list of command-line arguments.
        
    Returns:
        namespace: a namespace with attributes "number" and "precision". The
        value of each of these attributes will be a float.
    """
    parser = ArgumentParser()
    parser.add_argument("number", type=float,
                        help="number to compute the square root of")
    parser.add_argument("-p", "--precision", type=float, default=0.0000000001)
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print(f"The square root of {args.number} is approximately"
          f" {sqrt_b(args.number, args.precision)}")
