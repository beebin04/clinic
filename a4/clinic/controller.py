from .patient import Patient
from .exception.duplicate_login_exception import DuplicateLoginException
from .exception.illegal_access_exception import IllegalAccessException
from .exception.illegal_operation_exception import IllegalOperationException
from .exception.invalid_login_exception import InvalidLoginException
from .exception.invalid_logout_exception import InvalidLogoutException
from .exception.no_current_patient_exception import NoCurrentPatientException
from .dao.patient_dao_json import PatientDAOJSON
import hashlib

class Controller:
    #initialization  block
    def __init__(self, usrlogin=False, autosave=False):
        self.usrlogin = usrlogin
        self.current_patient : Patient = None
        self.userlist = self.read_users()
        self.autosave = autosave
        self.patient_dao = PatientDAOJSON(autosave)
    #login to the system with username and password  
    def read_users(self):
        with open("clinic/users.txt", "r") as fi:
            usrlist = {}
            for line in fi:
                details = line.strip().split(",")
                usrlist[details[0]] = details[1]
            return usrlist
    def login(self, usr : str, pswd : str):
        if self.usrlogin == True:
            raise DuplicateLoginException
        key = self.userlist.get(usr)
        pswd = hashlib.sha256(pswd.encode()).hexdigest()
        if key is not None and pswd == key:
            self.usrlogin = True
            return self.usrlogin
        else:
            raise InvalidLoginException
        
    #logout of the system  
    def logout(self):
        if self.usrlogin:
            self.usrlogin = False
            return True
        else:
            raise InvalidLogoutException
            
    #creates a patient object with a unique personal health number (phn), as well as other personal data 
    def create_patient(self, phn, n, b, p, e, a):
        if not self.usrlogin:
            raise IllegalAccessException
        if self.search_patient(phn):
            raise IllegalOperationException
        p = Patient(phn, n, b, p, e, a, self.autosave)
        self.patient_dao.create_patient(p)
        return p

            
    #searches for a patient by personal health number, returns the patient if successful 
    def search_patient(self, phn):
        if not self.usrlogin:
            raise IllegalAccessException
        p = self.patient_dao.search_patient(phn)
        if not p:
            return None
        return p
        
    #searches for a patient by name, returns a list
    def retrieve_patients(self, name):
        if not self.usrlogin:
            raise IllegalAccessException
        return self.patient_dao.retrieve_patients(name)
          
#searches for a patient by personal health number retrieves the patient data, and updates any part of the data     
       
    def update_patient(self, searchphn, phn, name, bd, phone, email, address):
        if not self.usrlogin:
            raise IllegalAccessException
        p = self.search_patient(phn)
        if p != None and searchphn != phn or self.search_patient(searchphn) is self.current_patient:
            raise IllegalOperationException
        updated_patient = Patient(phn, name, bd, phone, email, address, self.autosave)
        p = updated_patient
        return self.patient_dao.update_patient(searchphn, updated_patient)
    
    #searches a patient by personal health number and deletes it from the system        
    def delete_patient(self, phn):
        if not self.usrlogin:
            raise IllegalAccessException
        patient = self.search_patient(phn)
        if patient != None and patient != self.current_patient:
            return self.patient_dao.delete_patient(patient.phn)
        else:
            raise IllegalOperationException
    
    #returns a list of all patients
    def list_patients(self):
        if not self.usrlogin:
            raise IllegalAccessException
        return self.patient_dao.list_patients()
    
    #sets the current patient with a valid personal health number    
    def set_current_patient(self, phn):
        if not self.usrlogin:
            raise IllegalAccessException
        p = self.patient_dao.search_patient(phn)
        if not p:
            raise IllegalOperationException
        self.current_patient = p
    
    #returns the current patient
    def get_current_patient(self):
        if not self.usrlogin:
            raise IllegalAccessException
        return self.current_patient
    
    #sets the current patient to None
    def unset_current_patient(self):
        if self.usrlogin:
            self.current_patient = None
            return
        raise IllegalAccessException
        
    #creates a new note for the current patient's patient record, gives the note a code by incrementing a counter in patient record
    def create_note(self, note_details=str):
        if self.usrlogin:
            if self.current_patient != None:
                new_note = self.current_patient.create_note(note_details)
                return new_note
            else:
                raise NoCurrentPatientException
        raise IllegalAccessException
    
    #searches for a note by note code
    def search_note(self, note_code):
        if self.usrlogin:
            if self.current_patient != None:
                note = self.current_patient.search_note(note_code)
                return note
            raise NoCurrentPatientException
        raise IllegalAccessException
    
    #searches for all notes containing the given text and returns them as a list    
    def retrieve_notes(self, text):
        if self.usrlogin:
            if self.current_patient != None:
                li = self.current_patient.retrieve_notes(text)
                return li
            else:
                raise NoCurrentPatientException
        raise IllegalAccessException
    #updates the text body of a note
    def update_note(self, code: int, text: str):
        if self.usrlogin:
            if self.current_patient != None:
                return self.current_patient.update_note(code, text)
            else:
                raise NoCurrentPatientException
        raise IllegalAccessException
            
    #selects a note by code in the current patient's record and deletes it
    def delete_note(self, note_code):
        if self.usrlogin:
            if self.current_patient:
                note = self.current_patient.search_note(note_code)
                if note:
                    self.current_patient.delete_note(note.code)
                    return True
                return False
            raise NoCurrentPatientException
        raise IllegalAccessException
    
    #lists all the notes in the current patient record from last to first
    def list_notes(self) -> list:
        if self.usrlogin:
            li = []
            if self.current_patient != None:
                li = self.current_patient.list_notes()   
                return li
            raise NoCurrentPatientException
        raise IllegalAccessException
