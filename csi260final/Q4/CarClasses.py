def enforce_type(name, item, _type):
    if not isinstance(item, _type):
        raise TypeError(f"{name} must be a {_type}, not {type(item).__name__}")


class Cars:
    def __init__(self,
                 make : str,
                 model : str,
                 year : int,
                 type : str,
                 mpg : int,
                 cylinder : int,
                 turbo : bool,
                 hybrid : bool
                 ):
        enforce_type("make", make, str)
        enforce_type("model", model, str)
        enforce_type("year", year, int)
        enforce_type("type", type, str)
        enforce_type("mpg", mpg, int)
        enforce_type("cylinder", cylinder, int)
        enforce_type("turbo", turbo, bool)
        enforce_type("hybrid", hybrid, bool)

        self.make = make
        self.model = model
        self.year = year
        self.type = type
        self.mpg = mpg
        self.cylinder = cylinder
        self.turbo = turbo
        self.hybrid = hybrid


