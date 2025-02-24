"""Convert numbers from digits to words in Estonian."""


from argparse import ArgumentParser
import sys


LANGUAGES = [
    # uncomment "est" below if you implement Estonian numbers,
    # or "eus" if you implement Basque numbers
    
    "est",
    # "eus",
]


# replace this comment with your implementations of est() or eus() and main()
# (along with any helper functions, constants, etc. that you want to write)
def est(number): #Assume number will be an int 0 - 999 999
    pass

def parse_args(arglist):
    """Parse command-line arguments.
    
    Three arguments are required, in the following order:
    
        lang (str): the ISO 639-3 language code of the language the user wants
            to convert numbers into.
        input_file (str): path to a file containing numbers expressed as digits.
        output_file (str): path to a file where numbers will be written as words
            in the target language.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments as a namespace. The following attributes
        will be defined: lang, input_file, and output_file. See above for
        details.
    """
    parser = ArgumentParser()
    parser.add_argument("lang", help="ISO 639-3 language code")
    parser.add_argument("input_file", help="input file containing numbers")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.lang, args.input_file, args.output_file)
