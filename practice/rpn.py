from argparse import ArgumentParser
import sys


# Replace this comment with your implementations of the evaluate() and main()
# functions.
def evaluate(postfix_expression):
    pfix = "5 2 3 + *"
    pfix = pfix.split()
    possibleoperators = ['+','*','/','-']
    operators = []
    operands = []
    for element in pfix:
        if element in possibleoperators:
            operators.append(element)
        else:
            operands.append(float(element))
            
    print(operands)
    print(operators)

    operand1 = None
    operand2 = None

    i = 0
    while len(operands) != 1:
        #operand2 = operands.pop()
        #operand1 = operands.pop()
        operator = operators[i]
        i += 1
        match(operator):
            case('+'):
                operands.append(operands.pop() + operands.pop())
            case('*'):
                operands.append(operands.pop() * operands.pop())
            case('-'):
                operands.append(operands.pop() - operands.pop())
            case('/'):
                operands.append(operands.pop() / operands.pop())
                
        print(f"{operand1}{operator}{operand2}")


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
