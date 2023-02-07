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

    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.length = length

    def circumference(self):
        return 4 * self.length


class Circle(Form):
    """Circle Class: inherits from Form and has method area"""

    circles = []
    pi = 3.14159

    def __init__(self, diameter=1, x=0, y=0):
        super().__init__(x, y)
        self.diameter = diameter
        self.__class__.circles.append(self)

    def circumference(self):
        return self.diameter * self.__class__.pi

    @classmethod
    def circumferences(cls):
        """Class method to sum all circle circumferences."""
        csum = 0
        for c in cls.circles:
            csum = csum + c.circumference()
        return csum
