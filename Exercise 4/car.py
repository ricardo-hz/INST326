from math import cos, radians, sin


class Car:
    """Creates a car that can be turned and driven.
    
    Attributes:
        x: A float indicating the starting x position of the car. Default: 0.
        y: A float indicating the starting y position of the car. Default: 0.
        heading: A float indicating the starting direction of the car. 
            Default: 0.
    """
    
    def __init__(self, x = 0, y = 0, heading = 0):
        """ Initializes a Car object.
        
        Attributes:
            x: the starting x coordinate of the car, as a float. Default: 0.
            y: A float indicating starting y coordinate of the car. Default: 0.
            heading: A float indicating the starting direction of the car in 
                degrees. A value of 0 indicates north, 90 indicates east,
                180 indicates south, 270 indicates west. Default: 0.
            
        Side effects:
            Creates attributes for a car object.
        """
        
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, angle):
        """ Turns the car by a specified angle.

        Args:
            angle: A float representing the number of degrees by which the car
                object should be turned.
                
        Side effects:
            Modifies the car object's heading attribute.
        """
         
        self.heading += angle
        self.heading = self.heading%360
        
    def drive(self, distance):
        """ Moves a car object along an (x, y) axis.
        
        Args:
            distance: A float representing the number of degrees by which the
                car object should be moved.
            
        Side effects:
            Modifies the car object's x and y attributes. 
        """

        self.x += distance*sin(radians(self.heading))
        self.y -= distance*cos(radians(self.heading))


        
def sanity_check():
    """Tests the methods of the Car class.
    
    Side effects:
        Prints text to the console.
        
    Returns:
        A car object.
    """
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