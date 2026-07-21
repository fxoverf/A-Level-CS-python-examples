class patient: #class name
    __PatientName = "" #initialisation
    __PatientID = ""
    def __init__(self, Name, ID):
        self.__PatientName = Name
        self.__PatientID = ID
        patients.append(self)
    def getPatientName(self):
        return self.__PatientName
    def getPatientID(self):
        return self.__PatientID

patients = [] #array for patient data

for i in range(2):
    name = input("Enter Patient Name: ")
    ID = input("Enter Patient ID: ")

    patient(name, ID)


print("\nPatient Details")
for i in patients:
    print("Patient Name: ",i.getPatientName())
    print("Patient ID: ",i.getPatientID())