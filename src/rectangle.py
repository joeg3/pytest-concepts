

class Rectangle:
    """ Class representing a rectangle and operations on it """

    def __init__(self, length, witdh):
        self.length = length
        self.width = witdh
        self.area = 0

    def calculate_area(self):
        self.area = self.length * self.width
        return self.area