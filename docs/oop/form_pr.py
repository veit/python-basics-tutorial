"""form module. Contains the classes Form, Square and Circle"""


class Form:
    """Form class: has method move"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Square(Form):
    """Square Class:inherits from Form"""

    def __init__(self, length=1, x=0, y=0):
        super().__init__(x, y)
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    def circumference(self):
        return 4 * self.__length


class Circle(Form):
    """Circle Class: inherits from Form and has method area"""

    circles = []
    pi = 3.14159

    def __init__(self, diameter=1, x=0, y=0):
        super().__init__(x, y)
        self.__diameter = diameter
        self.__class__.circles.append(self)

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, new_diameter):
        self.__diameter = new_diameter

    def circumference(self):
        return self.diameter * self.__class__.pi

    @classmethod
    def circumferences(cls):
        """Class method to sum all circle circumferences."""
        csum = 0
        for c in cls.circles:
            csum = csum + c.circumference()
        return csum
