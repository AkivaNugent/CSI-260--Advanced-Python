"""Cylinder Class File."""
import math


class Cylinder:
    """Define Cylinder Object."""

    def __init__(self, radius: int, height: int):
        """Initialize cylinder."""
        self.radius = radius
        self.height = height

    def get_base(self):
        """Calculate base of cylinder."""
        return math.pi * self.radius * self.radius

    def get_s_area(self):
        """Calculate surface area of cylinder."""
        return math.pi * 2 * self.radius * (self.radius + (2 * self.height))

    def get_perimeter(self):
        """Calculate perimeter of cylinder."""
        return (math.pi * 2 * self.radius) + (2 * self.height)
