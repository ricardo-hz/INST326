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
    numbers = {
        0 : 'null',
        1 : 'üks',
        2 : 'kaks',
        3 : 'kolm',
        4 : 'neli',
        5 : 'viis',
        6 : 'kuus',
        7 : 'seitse',
        8 : 'kaheksa',
        9 : 'üheksa',
        10 : 'kümme',
        11 : 'üksteist',
        12 : 'kaksteist',
        13 : 'kolmteist',
        14 : 'neliteist',
        15 : 'viisteist',
        16 : 'kuusteist',
        17 : 'seitseteist',
        18 : 'kaheksateist',
        19 : 'üheksateist', 
        20 : 'kakskümmend',
        30 : 'kolmkümmend',
        40 : 'nelikümmend',
        50 : 'viiskümmend',
        60 : 'kuuskümmend',
        70 : 'seitsekümmend',
        80 : 'kaheksakümmend',
        90 : 'üheksakümmend',
        100 : 'sada',
        1000 : 'tuhat'
    }

    #Holds final translated string
    est = ""

    #Handle 6 digit numbers
    if len(str(number)) == 6:
        #Add first three digits of number to string
        est += (f'{numbers[number // 100_000]}{numbers[100]} ')
        number -= (number // 100_000 * 100_000)
        #Add "Thousand" to end of string if the next digits are zero
        if number == 0:
            est += (f'{numbers[1000]} ')

    # Handle 5 digit numbers 
    if len(str(number)) == 5:
        # Handle 'special' numbers (10 - 20)
        if number // 1000 in numbers:
            est += (f'{numbers[number // 1000]} {numbers[1000]} ')
            number -= number // 1000 * 1000
        # Handle nonspecial numbers
        else:
            est += (f'{numbers[number // 10_000 * 10]} ')
            number -= number // 10_000 * 10_000
            #Add 'thousand' to end of number
            if number == 0:
                est += (f'{numbers[1000]} ')

    # Handle 4 digit numbers
    if len(str(number)) == 4:
        #Handle 1000
        if number // 1000 * 1000 in numbers:
            est += (f'{numbers[number // 1000 * 1000]} ')
        #Handle all other 4 digit numbers
        else:
            est += (f'{numbers[number // 1000]} {numbers[1000]} ')
        number -= number // 1000 * 1000

    #Handle 3 digit numbers
    if len(str(number)) == 3:
        #Handle 100
        if number // 100 * 100 in numbers:
            est += (f'{numbers[number // 100 * 100]} ')
        #Handle all other 3 digit numbers
        else:
            est += (f'{numbers[number // 100]}{numbers[100]} ')
        number -= number // 100 * 100
    
    #Handle 2 digit numbers  
    if len(str(number)) == 2:
        # Handle 'special' numbers (10-20)
        if number in numbers:
            est += (f'{numbers[number]} ')
            number -= number
        # Handle all other numbers
        else:
            est += (f'{numbers[number // 10 * 10]} ')
            number -= number // 10 * 10

    #Handle non-zero one digit numbers
    if(len(str(number))) == 1 and number != 0:
        est += (f'{numbers[number]} ')
        number -= number

    #Handle zero
    if(len(str(number))) == 1 and not est:
        est += (f'{numbers[number]} ')
        number -= number
        
    return(est.strip())

def main(language_code, input_path, output_path):
    if language_code == 'est':
        with (open(input_path, 'r', encoding = 'UTF-8') as f_in, 
              open(output_path, 'w', encoding = 'UTF-8') as f_out):
                for line in f_in:
                    f_out.write(f'{line.strip()} = {est(int(line))}\n')
    else:
        raise ValueError()

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
