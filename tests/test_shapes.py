import pytest
from polygon.shapes import Point2D, Line


class TestTypes:
    p = Point2D(2, 3)
    q = Point2D(3, 6)
    line: Line = Line(p, q)
       
    def test_slope(self):
        assert self.line.slope() == 3
    
    def test_y_intercept(self):
        assert self.line.y_intercept() == -3