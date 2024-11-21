from abc import ABC, abstractmethod
class PatientDAO(ABC):
    @abstractmethod
    #deffers to PatientDaoJson, which searches for a patient using their personal health number (PHN)
    def search_patient(self, key):
        pass
    @abstractmethod
    #deffers to PatientDaoJson, which creates a new patient with a unique PHN
    def create_patient(self, patient):
        pass
    @abstractmethod
    #deffers to PatientDaoJson, which searches for patients with a name that contains the input string and returns them as a list
    def retrieve_patients(self, search_string):
        pass
    @abstractmethod
    #deffers to PatientDaoJson, which searches for a patient by PHN and updates any of its data fields
    def update_patient(self, key, patient):
        pass
    @abstractmethod
    #deffers to PatientDaoJson, which searches for a patient by PHN and deletes it from the list of patients and removes it from the savefile
    def delete_patient(self, key):
        pass
    @abstractmethod
    #deffers to PatientDaoJson, which returns a list of all patients
    def list_patients(self):
        pass

