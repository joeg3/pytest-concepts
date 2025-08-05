

class Rectangle:
    """ Class representing a rectangle and operations on it """

    def __init__(self, length, witdh):
        self.length = length
        self.width = witdh
        self.area = 0
        self.version = 2 # Software version of this class

    def calculate_area(self):
        self.area = self.length * self.width
        return self.area