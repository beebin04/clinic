from abc import ABC, abstractmethod
class PatientDAO(ABC):
    @abstractmethod
    #deffers to PatientDaoJson
    def search_patient(self, key):
        pass
    @abstractmethod
    #deffers to PatientDaoJson
    def create_patient(self, patient):
        pass
    @abstractmethod
    #deffers to PatientDaoJson
    def retrieve_patients(self, search_string):
        pass
    @abstractmethod
    #deffers to PatientDaoJson
    def update_patient(self, key, patient):
        pass
    @abstractmethod
    #deffers to PatientDaoJson
    def delete_patient(self, key):
        pass
    @abstractmethod
    #deffers to PatientDaoJson
    def list_patients(self):
        pass

