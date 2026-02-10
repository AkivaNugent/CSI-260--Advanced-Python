class Country:
    """Country Class"""
    def __init__(self, name : str, population : int, area : int):
        self.name = name
        self.population = population
        self.area = area


    def is_larger(self, opp):
        """Compare country size with a passed oppositional country"""

        if self.area > opp.area:
            return True
        return False


    def population_density(self):
        """calculate population density"""

        return self.population / self.area


    def summary(self):
        """Provide summary of Country"""

        return (f'{self.name} has a population of {self.population} people '
                f'and is {self.area} square km. It therefore has a population '
                f'density of {self.population_density():.4f} people per square km.')

