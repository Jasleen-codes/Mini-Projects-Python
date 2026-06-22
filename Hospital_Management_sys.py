# Hospital Management System

# List to maintain patient IDs
patient_ids = []

# Dictionary to store patient records
patients = {}
 # Patient Class 
 
class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print("\nPatient Details")
        print("ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


#Doctor Class 
class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        print("\nDoctor Details")
        print("Doctor ID:", self.doctor_id)
        print("Name:", self.name)
        print("Specialization:", self.specialization)


# Add Patient 
def add_patient():
    try:
        patient_id = input("Enter Patient ID: ")

        if patient_id in patient_ids:
            raise ValueError("Patient ID already exists!")

        name = input("Enter Patient Name: ")

        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError("Age must be positive!")

        disease = input("Enter Disease: ")

        patient = Patient(patient_id, name, age, disease)

        patient_ids.append(patient_id)

        patients[patient_id] = {
            "Name": name,
            "Age": age,
            "Disease": disease
        }

        save_record(patient)

        print("Patient added successfully!")

    except ValueError as e:
        print("Error:", e)


#Save Records to File 
def save_record(patient):
    with open("patients.txt", "a") as file:
        file.write(
            f"{patient.patient_id}, "
            f"{patient.name}, "
            f"{patient.age}, "
            f"{patient.disease}\n"
        )


# Display Patients 
def display_patients():
    if not patients:
        print("No patient records found!")
        return

    print("\nPatient Records")
    for pid, details in patients.items():
        print(f"\nPatient ID: {pid}")
        for key, value in details.items():
            print(f"{key}: {value}")


# Search Patient
def search_patient():
    pid = input("Enter Patient ID to search: ")

    if pid in patients:
        print("\nPatient Found")
        print(patients[pid])
    else:
        print("Patient not found!")

def schedule_appointment():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return

    doctor_name = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date: ")

    with open("appointments.txt", "a") as file:
        file.write(
            f"Patient ID: {pid}, "
            f"Doctor: {doctor_name}, "
            f"Date: {date}\n"
        )

    print("Appointment Scheduled Successfully!")

while True:
    print("\n--- HOSPITAL MANAGEMENT SYSTEM ----")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Schedule Appointment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        display_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        schedule_appointment()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")