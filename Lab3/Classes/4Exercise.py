import math

class Point:
    def __init__(self , x=0 , y=0):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"Coordinates: ({self.x} , {self.y})")
        
    def move(self , deltax , deltay):
        self.x = deltax
        self.y = deltay
        
    def distance(self , other_point):
        return math.sqrt((self.x - other_point.x)**2 +(self.y - other_point.y)**2)
    
    
point1 = Point(int(input()) , int(input()))
point2 = Point(int(input()) , int(input()))
point1.show()
point1.move(int(input()) , int(input()))
distance = point1.distance(point2)
        
    
    