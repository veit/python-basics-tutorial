"""shape module. Contains classes Form, Square and Circle"""
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
        Form.__init__(self, x, y)
        self.side = side
class Circle(Form):
    """Circle Class: inherits from Form and has method area"""
    pi = 3.14159
    def __init__(self, r=1, x=0, y=0):
        Form.__init__(self, x, y)
        self.radius = r
    def area(self):
        """Circle area method: returns the area of the circle."""
        return self.radius * self.radius * self.pi
    def __str__(self):
        return "Circle of radius %s at coordinates (%d, %d)"\
               % (self.radius, self.x, self.y)
