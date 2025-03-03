"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys


class PlayerWords:
    '''Gets a path to a text file for a game and calculates the score
    
    Attributes:
        words (set of strings): players words
    '''
    def __init__(self, path):
        '''creates a PlayerWords object with a word set
        
        Args:
            path (string): path to a text document with the player's words
        
        Side effects:
            creates a PlayerWords object with a set of the player's words
        '''
        self.words = set()
        
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip().lower()
                self.words.add(line)
                
    def score(self, player2):
        '''checks the score of the player with another player object
        
        Args:
            player2 (PlayerWords): second player to compare words to 
        
        Returns:
            score as an int
        '''
        
        score = int()
        
        for word in player2.words & self.words:
            if(len(word) > 2):
                score += len(word) - 2
                
        return score
    
    
    
def main(p1_words, p2_words):
    '''takes 2 files as an input, makes them PlayerWords objects,
        checks their score and prints it
        
    Args:
        p1_words (string): path to player 1's word txt file
        p2_words (string): path to player 2's word txt file

    Side effects:
        prints out the team's score
    '''
    p1 = PlayerWords(p1_words)
    p2 = PlayerWords(p2_words)
    
    print(f'Your team scored {p1.score(p2)} points!')


def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
