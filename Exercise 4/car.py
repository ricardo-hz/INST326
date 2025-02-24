from math import cos, radians, sin


class Car:
    '''creates a car that can be turned and driven
    
    Attributes:
        x (float): the starting x coordinate of the car, as a float. Default: 0.
        y (float): the starting y coordinate of the car, as a float. Default: 0.
        heading (float): the starting heading, as a float. Default: 0.
    '''
    
    def __init__(self, x = 0, y = 0, heading = 0):
        ''' initializes a Car object with x-y coordinates and a heading,
            all defaulting at 0
        
        Attributes:
            x (float): the starting x coordinate of the car, as a float. Default: 0.
            y (float): the starting y coordinate of the car, as a float. Default: 0.
            heading (float): the starting heading, as a float. Default: 0.
            
        Side effects:
            none
            
        Returns:
            none
        '''
        
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, angle):
        ''' Turns the car by a specified angle

        Attributes:
            angle (float): angle to turn the car by in degrees
            
        Side effects:
            changes the heading value of the Car object

        Returns:
            none
        '''
         
        self.heading += angle
        
        self.heading = self.heading%360
        
    def drive(self, distance):
        ''' moves car by a specified distance
        
        Attributes:
            distance (float): distance to move the car by
            
        Side effects:
            changes the x and y values of the Car object

        Returns:
            none
        '''
        
        self.x += distance*sin(radians(self.heading))
        self.y -= distance*cos(radians(self.heading))


        
def sanity_check():
    c = Car()
    c.turn(90)
    c.drive(10)
    c.turn(30)
    c.drive(20)
    print(f'Location: {c.x}, {c.y}')
    print(f'Heading: {c.heading}')
    
    return c


if __name__ == "__main__":
    sanity_check()