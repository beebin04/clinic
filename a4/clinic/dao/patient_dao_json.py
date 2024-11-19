from .patient_decoder import PatientDecoder
from .patient_dao import PatientDAO
from json import load, dump, decoder
from .patient_encoder import PatientEncoder
class PatientDAOJSON(PatientDAO):
    #initialization block
    def __init__(self, autosave=False):
        self.autosave = autosave
        self.filename = 'clinic/patients.json'
        if self.autosave:
            #here we try to open the file storing the patients
            try:
                with open(self.filename, 'r') as file:
                    self.patients = load(file, cls=PatientDecoder)
            except (FileNotFoundError, decoder.JSONDecodeError):
                self.patients = []
        else:
            self.patients = []
    #searches for a patient by their personal health number(PHN)        
    def search_patient(self, key):
        for patient in self.patients:
                if patient.phn == key:
                    return patient
        return None
    #creates a new patient in the file with a unique PHN
    def create_patient(self, patient):
        if not self.search_patient(patient.phn):
            self.patients.append(patient)
            if self.autosave:
                with open(self.filename, 'w') as file:
                    dump(self.patients, file, cls=PatientEncoder, indent=4)
            return True
        return False
    #searches for patients with a name that contains the input string and returns them as a list 
    def retrieve_patients(self, search_string : str):
        result = []
        for patient in self.patients:
            if search_string in patient.name:
                result.append(patient)
        return result
    #searches for a patient by PHN, and updates any of its data fields
    def update_patient(self, key, patient):
        existing_patient = self.search_patient(key)
        if existing_patient:
            existing_patient.phn = patient.phn
            existing_patient.name = patient.name
            existing_patient.birth_date = patient.birth_date
            existing_patient.phone = patient.phone
            existing_patient.email = patient.email
            existing_patient.address = patient.address
            if self.autosave:
                with open(self.filename, 'w') as file:
                    dump(self.patients, file, cls=PatientEncoder, indent=4)
            return True
        return False
    #searches for a patient by PHN deletes it from the list of patients, and removes it from the file
    def delete_patient(self, key):
        target_patient = self.search_patient(key)
        if target_patient:
            self.patients.remove(target_patient)
            if self.autosave:
                with open(self.filename, 'w') as file:
                    dump(self.patients, file, cls=PatientEncoder, indent=4)
            return True
        return False
    #returns a list of all patients
    def list_patients(self):
        plist = []
        for patient in self.patients:
            plist.append(patient)
        return plist
