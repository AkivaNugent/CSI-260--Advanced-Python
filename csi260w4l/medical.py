"""Define Patient and Producre Classes.

Author: Akiva Nugent
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 13, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import pickle


class Patient:
    """Define patient class."""

    _next_id = 1
    _all_patients = {}

    def __init__(self, first_name, last_name, address,
                 phone_number, ec_name, ec_phone_number):
        """Construct patient object."""
        self.patient_id = Patient._next_id
        Patient._next_id += 1
        self.procedures = []
        Patient._all_patients[self.patient_id] = self

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.ec_name = ec_name
        self.ec_phone_number = ec_phone_number

    def __str__(self):
        """Provide string representation for patient information."""
        result = (
            f"  Patient No. #{self.patient_id}\n"
            f"     Name: {self.first_name} {self.last_name}\n"
            f"     Address: {self.address}\n"
            f"     Phone: {self.phone_number}\n"
            f"     Emergency Contact: ${self.ec_name} : "
            f"{self.ec_phone_number}\n"
            f"\n"
            f" Procedures: \n"
        )
        if self.procedures:
            for procedure in self.procedures:
                result += str(procedure) + "\n"
        else:
            result += 'This patient has no procedures scheduled. \n'

        return result

    def add_procedure(self, procedure):
        """Add a procedure to the patient."""
        self.procedures.append(procedure)

    @classmethod
    def get_patient(cls, patient_id):
        """Retrieve a patient's record by ID."""
        return cls._all_patients.get(patient_id, None)

    @classmethod
    def delete_patient(cls, patient_id):
        """Delete a patient's record."""
        if patient_id in cls._all_patients:
            del cls._all_patients[patient_id]

    @classmethod
    def save_patient(cls, filename="patients.pkl"):
        """Save the patients records to a pickle file."""
        """
        The following YT video was used for refreshing my knowing of pickle
        files. This is pretty bog standard, but it is also very close to his
        code so im directly linking it here :).
        https://www.youtube.com/watch?v=6Q56r_fVqgw
        """
        with open(filename, "wb") as file:
            pickle.dump({
                "patients": cls._all_patients,
                "next_patient_id": cls._next_id,
                "next_procedure_id": Procedure._next_id
            }, file)
            print("Records saved. ")

    @classmethod
    def load_patients(cls, filename="patients.pkl"):
        """Load the patient records from pickle file."""
        """
        The following YT video was used for refreshing my knowing of pickle
        files. This is pretty bog standard, but it is also very close to his
        code so im directly linking it here :).
        https://www.youtube.com/watch?v=6Q56r_fVqgw
        """
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            cls._all_patients = data["patients"]
            cls._next_id = data["next_patient_id"]
            Procedure._next_id = data["next_procedure_id"]


class Procedure:
    """Define a procedure."""

    _next_id = 1

    def __init__(self, name, date, practitioner, cost):
        """Construct Procedure Class."""
        self.procedure_id = Procedure._next_id
        Procedure._next_id += 1

        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.cost = cost

    def __str__(self):
        """Give a string representation of the class."""
        return (
            f"  Procedure No. #{self.procedure_id}\n"
            f"     Name: {self.name}\n"
            f"     Date: {self.date}\n"
            f"     Practitioner: {self.practitioner}\n"
            f"     Cost: ${self.cost}\n"
        )
