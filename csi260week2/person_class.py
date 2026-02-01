from symtable import Class


class Student:
    def __init__(self,
                 _first_name = "[FIRSTNAME]",
                 _last_name = "[LASTNAME]",
                 _year = "[YEAR]",
                 _major = "[MAJOR]",
                 _minor = "[MINOR]"
                 ):
        self._first_name = _first_name
        self._last_name = _last_name
        self._year = _year
        self._major = _major
        self._minor = _minor

    def get_full_name(self):
        _full_name = self._first_name + " " + self._last_name
        return _full_name

    


blank = Student()
akiva = Student("akiva", "nugent", 3, "CS", "maths")
print(blank.get_full_name())
print(akiva.get_full_name())
