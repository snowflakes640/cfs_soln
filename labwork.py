patients = []

class Hospital():
    
    def __init__(self):
        pass

    def add_p(self, id, name, disease, date):
        new_p = {"ID": id,
                 "Name": name,
                 "Disease": disease,
                 "Date": date}
        patients.append(new_p)
    
    def show():
        print(patients)

    def find(id):
        for patient in patients:
            if id == patient["ID"]:
                print(patient)

    def delete(id):
        for patient in patients:
            if id == patient["ID"]:
                patients.remove(patient)
    
    def update(self, name, info_type, new_info):
        for patient in patients:
            if name == patient["Name"]:
                patient[info_type] = new_info
    


patient1 = Hospital()
patient2 = Hospital()

#Adding new patients:
patient1.add_p(157,"Maliha","BPD","11/10/2020")
patient2.add_p(333, "Rain", "Clinical depreseion", "02/05/2020")

#Displaying the list of patients:
print("\nThe list of current patients is:")
Hospital.show()
print("\n")

#Searching a patient using the id:
print("Information about patient with id 001:")
Hospital.find(157)
print("\n")

#Deleting information about a patient:
Hospital.delete(333)
print("Deletation successful\n")

#Updating information of a patient:
patient1.update("Maliha", "Disease", "Schizophrenia")
print("Info updated\n")

print(patients)