#https://medium.com/analytics-vidhya/python-name-mangling-and-how-to-use-underscores-e67b529f744f 
from foo import *
class Square:

    def __init__(self, length):
        self._side = length
        self._area = length**2

    @property
    def area(self):
        return self._area

    @property
    def height(self):
        return self._side
    
    @height.setter
    def height(self, length):
        self._side = length
        self._reset_area()

    @property
    def width(self):
        return self._side

    @width.setter
    def width(self, length):
        print("i am here 111\n")
        self._side = length
        self._reset_area()

    def _reset_area(self):
        self._area = self._side**2


sq = Square(5)
print(sq.height) # 5
print(sq.area) # 25

sq._side = 10 # Bad approach, will not recalculate area
print(sq.height) # 10 - what we would expect
print(sq.area) # 25 - we would expect 100

sq.width = 10 # Correct approach "def width(self, length):" get called.
print(sq.height) # 10 - what we would expect
print(sq.area) # 100 - cool, as expected

public_method()
#_private_method()

foo = Foo()
#print(foo.__bar)