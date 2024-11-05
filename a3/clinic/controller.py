from .patient import Patient
class Controller:
    #initialization  block
    def __init__(self, usrlogin=False):
        self.usrlogin = usrlogin
        self.current_patient = None
        self.patient_list =[]
    #login to the system with username and password  
    def login(self, usr, pswd):
        if self.usrlogin == True:
            return False 
        if usr == "user" and pswd == "clinic2024":
            self.usrlogin = True
        return self.usrlogin
        
    #logout of the system  
    def logout(self):
        if self.usrlogin:
            self.usrlogin = False
            return True
        else:
            return False
            
    #creates a patient object with a unique personal health number (phn), as well as other personal data 
    def create_patient(self, phn, n, b, p, e, a):
        if self.search_patient(phn) == None:
            if self.usrlogin:
                p = Patient(phn, n, b, p, e, a)
                self.patient_list.append(p)
                return p
            else:
                return None
        else: 
            return None
            
    #searches for a patient by personal health number, returns the patient if successful 
    def search_patient(self, phn):
        if self.usrlogin:
            for patient in self.patient_list:
                if patient.phn == phn:
                    return patient
        return None
        
    #searches for a patient by name, returns a list
    def retrieve_patients(self, name):
        if self.usrlogin:
            result = []
            for patient in self.patient_list:
                if name in patient.name:
                    result.append(patient)
            return result
        else:
            return None
    #searches for a patient by personal health number retrieves the patient data, and updates any part of the data     
       
    def update_patient(self, searchphn, phn, name, bd, phone, email, address):
        if self.usrlogin:
            if self.search_patient(phn) != None and searchphn != phn:
                return False
            pat = self.search_patient(searchphn)
            if pat != None and pat != self.current_patient:
                pat.phn = phn
                pat.name = name
                pat.birth_date = bd
                pat.phone = phone
                pat.email = email
                pat.address = address
                return True
        else:
            return False
            
    #searches a patient by personal health number and deletes it from the system        
    def delete_patient(self, phn):
        if self.usrlogin is False:
            return False
        patient = self.search_patient(phn)
        if patient != None and patient != self.current_patient:
            self.patient_list.remove(patient)
            return True
        else:
            return False
    
    #returns a list of all patients
    def list_patients(self):
        if self.usrlogin:
            li = []
            for p in self.patient_list:
                li.append(p)
            return li
        return None
    #sets the current patient with a valid personal health number    
    def set_current_patient(self, phn):
        if self.usrlogin:
            p = self.search_patient(phn)
            if p is not None:
                self.current_patient = p
        return None
    
    #returns the current patient
    def get_current_patient(self):
        if self.usrlogin:
            return self.current_patient
        return None
    
    #sets the current patient to None
    def unset_current_patient(self):
        self.current_patient = None
        return
        
    #creates a new note for the current patient's patient record, gives the note a code by incrementing a counter in patient record
    def create_note(self, note_details=str):
        if self.usrlogin:
            if self.current_patient != None:
                new_note = self.current_patient.patient_record.create_note(note_details)
                return new_note
        return None
    
    #searches for a note by note code
    def search_note(self, note_code):
        if self.usrlogin:
            if self.current_patient != None:
                note = self.current_patient.patient_record.search_note(note_code)
                return note
        return None
    
    #searches for all notes containing the given text and returns them as a list    
    def retrieve_notes(self, text):
        if self.usrlogin:
            if self.current_patient != None:
                li = self.current_patient.patient_record.retrieve_notes(text)
                return li
        return None
    #updates the text body of a note
    def update_note(self, code: int, text: str):
        if self.usrlogin:
            if self.current_patient != None:
                return self.current_patient.patient_record.update_note(code, text)
            
    #selects a note by code in the current patient's record and deletes it
    def delete_note(self, note_code):
        if self.usrlogin:
            if self.current_patient != None:
                self.current_patient.patient_record.delete_note(note_code)
                return True
        return  None
    
    #lists all the notes in the current patient record from last to first
    def list_notes(self):
        if self.usrlogin:
            if self.current_patient != None:
                li = self.current_patient.patient_record.list_notes()    
                return li
        return None
