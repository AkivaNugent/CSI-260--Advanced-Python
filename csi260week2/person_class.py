#How to create and work with an object (class)

class Student():    #This is an object name

    # Class variables: These are shared with all students
    honors_inc = float(input("Enter the honors increase differential (use decimals): "))
    num_of_students = 0

    def __init__(self, fn, ln, year, major, minor, gpa):  #This is the constructor
        self.fn = fn        #This is an instance variable
        self.ln = ln
        self.year = year
        self.major = major
        self.minor = minor
        self.gpa = gpa

        Student.num_of_students += 1

    def apply_honors(self): #Regular method
        self.gpa = float(self.gpa * self.honors_inc) #Resetting a variable value

    @classmethod
    def set_honors_inc(clscls, amt):
        pass

    def reset(self): ##Regular method
        self.fn = ''
        self.ln = ''
        self.year = 0
        self.major = 'undeclared'
        self.minor = 'undeclared'
        self.gpa = 0


    #Add an action/method
    def addFullName(self): #Regular method
        return '{} {}'.format(self.fn, self.ln)

#Instances of the object
s1 = Student('John', 'Doe', 2, 'CSI', 'CNCS', 3.1)
s2 = Student('Jane', 'Smith', 3, 'CNCS', 'CSI', 3.5)

<<<<<<< Updated upstream
    
=======
print(s1.addFullName())
print(s2.addFullName())
print(Student.addFullName(s2))
#s1.reset()
print("No data here:",s1.addFullName())
>>>>>>> Stashed changes

'''
Code using the class varialbe apply_honors
'''
print(s2.gpa)
s2.apply_honors()
print("GPA with honors differential applied to the GPA:",s2.gpa)

#Printing a namespace
print(s2.__dict__)
print(Student.__dict__)

s2.honors_inc = 1.5 #Overriding a class variable
print(s2.__dict__)
print(Student.honors_inc)
print(s1.honors_inc)
print(s2.honors_inc)

print("Total number of students equals:",Student.num_of_students)