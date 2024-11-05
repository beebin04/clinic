from patient_record import PatientRecord
from notes import Note
class Patient():
    #initialization block
    def __init__(self, 
                phn: int = None,
                n: str = None,
                b: str = None,
                p: str = None,
                e: str = None,
                a: str = None):
            self.phn = phn
            self.name = n
            self.birth_date = b
            self.phone = p
            self.email = e
            self.address = a
            self.patient_record = PatientRecord()
    #returns the representation of patient        
    def __repr__(self):
        return "Patient(%d, %s, %s, %s, %s, %s)" % (self.phn, self.name, self.birth_date, self.phone, self.email, self.address)
    
    #checks for equality
    def __eq__(self, other):
        if other != None:
            if self.phn != other.phn:
                return False
            if self.name != other.name:
                return False
            if self.birth_date != other.birth_date:
                return False
            if self.phone != other.phone:
                return False
            if self.email != other.email:
                return False
            if self.address != other.address:
                return False
            return True
        return False
    
    #creates a new note for the current patient's patient record, gives the note a code by incrementing a counter in patient record
    def create_note(self, txt: str):
        return self.patient_record.create_note(txt)
   
   #searches for a note by note code
    def search_note(self, code: int):
        return self.patient_record.search_note(code)
   
   #updates the text body of a note
    def update_note(self, code: int, text: str):
        return self.patient_record.update_note(code, text)
        
    #selects a note by code and deletes it
    def delete_note(self, code: int):
        return self.patient_record.delete_note(code)
        
    #searches for all notes containing the given text and returns them as a list            
    def retrieve_notes(self, text):
        return self.patient_record.retrieve_notes(text)
        
    #lists all the notes in the current patient record from last to first        
    def list_notes(self): 
        return self.patient_record.list_notes()
