"""Define the behavior for our medical system.

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


from medical import Patient, Procedure

DATA = "patients.pkl"


def load_data():
    """Load patient data from file."""
    try:
        Patient.load_patients(DATA)
        print("patients loaded properly.")
    except FileNotFoundError:
        print("file does not exist. New file created.")


def add_patient():
    """Add a new patient."""
    print("\nADD A NEW PATIENT: ")
    patient = Patient(input("First name: "),
                      input("Last name: "),
                      input("Address: "),
                      input("Phone Number: "),
                      input("Emergency Contact - Name: "),
                      input("Emergency Contact - Phone Number: "),
                      )
    print(f"\n Patient (ID # {patient.patient_id}) Added to system")


def edit_patient(patient):
    """Edit patient information."""
    print("\nEDIT PATIENTS INFORMATION: ")
    print("  What information would you like to change? ")
    print("   1. First name")
    print("   2. Last name")
    print("   3. Address")
    print("   4. Phone")
    print("   5. Emergency contact name")
    print("   6. Emergency contact phone")

    selection = input("Enter Selection (1-6): ").strip()
    if selection == "1":
        patient.first_name = input("New first name: ")
    elif selection == "2":
        patient.last_name = input("New Last name: ")
    elif selection == "3":
        patient.address = input("New address: ")
    elif selection == "4":
        patient.phone_number = input("New phone name: ")
    elif selection == "5":
        patient.ec_name = input("New emergency contact name: ")
    elif selection == "6":
        patient.ec_phone_number = input("New emergency contact phone number: ")
    else:
        print("Invalid Choice.")
        return
    print("Patient updated")


def add_procedure(patient):
    """Add procedure to a given patient."""
    print("\n ADD A PROCEDURE:")
    procedure = Procedure(input("Procedure Name: "),
                          input("Scheduled date: "),
                          input("Doctor Name: "),
                          input("Cost: $")
                          )
    patient.add_procedure(procedure)
    print(f" Procedure (ID #{procedure.procedure_id}) added")


def patient_menu(patient):
    """Show options for selected patient."""
    print(f"\n {patient}")

    while True:
        print("\n PATIENT MENU")
        print("  1. Edit patient data")
        print("  2. Delete patient")
        print("  3. Add a procedure")
        print("  4. Back to main menu")

        selection = input("Enter Choice (1-4)").strip()

        if selection == "1":
            edit_patient(patient)
        elif selection == "2":
            patient.delete_patient(patient.patient_id)
        elif selection == "3":
            add_procedure(patient)
        elif selection == "4":
            return
        else:
            print("Invalid choice. Please try again")


def patient_lookup():
    """Display patient data from prompted ID."""
    try:
        patient_id = int(input("Enter patient ID number: "))
    except ValueError:
        print("Invalid ID. please enter an integer.")
        return
    patient = Patient.get_patient(patient_id)
    if patient is None:
        print(f"No patient found with ID # {patient_id}")
    else:
        patient_menu(patient)


def main():
    """Define main driving function."""
    load_data()
    while True:
        print("\n ---------HOSPITAL PATIENT SYSTEM -----------")
        print("1. Look up a patient by ID")
        print("2. Add a new patient")
        print("3. Quit")

        selection = input("Enter selection (1-3): ").strip()

        if selection == "1":
            patient_lookup()
        elif selection == "2":
            add_patient()
        elif selection == "3":
            Patient.save_patient(DATA)
            print("Goodbye :)")
            break
        else:
            print("invalid selection. Please try again.")


if __name__ == "__main__":
    main()
