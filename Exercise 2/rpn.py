from argparse import ArgumentParser
import sys
#TODO: Make main method
#TODO: Read from file
#TODO: Print steps

# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(postfix_expression):
    postfix_expression = postfix_expression.strip().split()
    possibleoperators = ['+','*','/','-']
    operators = []
    operands = []
    for element in postfix_expression:
        if element in possibleoperators:
            operators.append(element)
        else:
            operands.append(float(element))

    i = 0
    while len(operands) != 1:
        operand2 = operands.pop()
        operand1 = operands.pop()
        match(operators[i]):
            case('+'):
                operands.append(operand1 + operand2)
            case('*'):
                operands.append(operand1 * operand2)
            case('-'):
                operands.append(operand1 - operand2)
            case('/'):
                operands.append(operand1 / operand2)
        i += 1         
    return(operands[0])


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
