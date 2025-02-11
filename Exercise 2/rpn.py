from argparse import ArgumentParser
import sys

def evaluate(postfix_expression):
    """Evaluates expressions written in postfix notation.
    
    Args:
        postfix_expression (str) : Postfix expression to be evaluted.
    
    Returns:
        float : The result of evaluating the postfix expression.
    
    Raises:
        IndexError : Passed an expression without proper postfix notation.
    """
    operands = []
    possible_operators = ['+','*','/','-']
    postfix_expression = postfix_expression.strip().split()
    
    #Loop through each character in the given postfix expression
    for element in postfix_expression:
        #Add number elements to stack
        if not element in possible_operators:
            operands.append(float(element))
        #Do postfix calculation with stack when operator found
        else:
            #Get operands
            try:
                operand2 = operands.pop()
                operand1 = operands.pop()
            #Handle invalid postfix expressions being passed
            except:
                print(f"There was an issue, please check "
                      f"your postfix expression.")
                raise
            #Add result of postfix calculation to stack
            match(element):
                case("+"):
                    operands.append(operand1 + operand2)
                case("*"):
                    operands.append(operand1 * operand2)
                case("-"):
                    operands.append(operand1 - operand2)
                case("/"):
                    operands.append(operand1 / operand2)
    
    #Return result of postfix calculation
    if(len(operands) == 1):
        return operands[0]
    #Final check for if the postfix expression is valid
    else:
        print("There was an issue, please check your postfix expression.")
        raise
    
def main(path):
    """Reads postfix expressions from a file, prints results to console.
    
    Args:
        path(str) : The path that the postfix expressions should be read from.
    
    Side Effects:
        - Prints the contents of the file to the console, followed by "=" and
            the return value given by the evaluate function
    """
    with open(path, "r", encoding = "utf-8") as f:
        for line in f:
            print(f"{line.strip()} = {evaluate(line.strip())}")


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
