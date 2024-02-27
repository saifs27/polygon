import numpy as np
from dataclasses import dataclass
from enum import Enum

class Orientation(Enum):
    COLINEAR = 1
    LEFT_TURN = 2
    RIGHT_TURN = 3


@dataclass
class Point2D:
    x: float
    y: float

@dataclass    
class Line:
    p: Point2D
    q: Point2D
    
    def length(self) -> float:
        return np.sqrt((self.p.x - self.q.x)**2 + (self.p.y - self.q.y)**2)
    
    def midpoint(self) -> Point2D:
        x: float = (self.p.x + self.q.x) / 2
        y: float = (self.p.y + self.q.y) / 2
        return Point2D.p(x, y)
    
    def slope(self) -> float:
        y_delta: float = self.p.y - self.q.y
        x_delta: float = self.p.x - self.q.x
        return y_delta / x_delta
    def y_intercept(self) -> float:
        m: float = self.slope()
        return  (m * (-self.p.x)) + self.p.y
    

@dataclass
class Vector2D:
    ...

@dataclass  
class Circle:
    radius: float

    def area(self) -> float:
        return np.pi * (self.radius**2)
    
    def circumference(self) -> float:
        return np.pi * 2 * self.radius
    
    def diameter(self) -> float:
        return 2 * self.radius
    
    
    

@dataclass
class Triangle:
    x: Point2D
    y: Point2D
    z: Point2D

    def area(self) -> float:
        base: Line = Line(self.x, self.y)
        height: Line = Line(base.midpoint(), self.z)
        return (1/2) * (base.length() * height.length())
    
    def midpoint(self) -> Point2D:
        ...
    
        
def orientation(p: Point2D, q: Point2D, m: Point2D) -> Orientation:
    first_line: Line = Line(p, q)
    
    y: float = first_line.slope() * m.x + first_line.y_intercept()
    
    if m.y > y:
        return Orientation.LEFT_TURN
    elif m.y < y:
        return Orientation.RIGHT_TURN
    else:
        return Orientation.COLINEAR
    
    
