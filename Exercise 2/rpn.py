from argparse import ArgumentParser
import sys
#TODO: Make main method
#TODO: Read from file
#TODO: Print steps

# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(postfix_expression):
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
                print("There was an issue, please check your postfix expression.")
                return None
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
        return None


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
