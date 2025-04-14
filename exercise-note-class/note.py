POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


## Replace this comment with your implementation of the Note class
class Note():
    def __init__(self, note, perspective = None):
        """Initializes a note object
        """
        if isinstance(note,str):
            self.position = POSITIONS[note]
        else:
            self.position = note
            
        self.perspective = perspective
    
    #Inversion
    def __invert__(self):
        if not isinstance(self, Note):
            raise TypeError(f"{self} is not a Note object")
        
        if self.perspective == "#":
            Note(self.position, "b")
        
        if self.perspective == "b":
            Note(self.position, "*")

        if self.perspective == None:
            Note(self.position)
            
    #Addition
    def __add__(self, other):
        self.position = (self.position + other) % 11 
        
        
    #Subtraction
    #Right shift
    #Left shift
    #(in)formal representation
