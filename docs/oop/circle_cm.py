"""circle module: contains the 'Circle' class"""


class Circle:
    """Circle class.

    The class variable 'circles' contains a list of all circle instances.

    """

    circles = []
    pi = 3.14159

    def __init__(self, diameter=1):
        """Create a Circle instance with a given diameter and add an initialised
        circle to the circles list."""
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
