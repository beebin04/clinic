from .patient_record import PatientRecord
from .notes import Note
class Patient():
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
            
    def __repr__(self):
        return "Patient(%d, %s, %s, %s, %s, %s)" % (self.phn, self.name, self.birth_date, self.phone, self.email, self.address)
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
    
    def create_note(self, txt: str):
        return self.patient_record.create_note(txt)
    
    def search_note(self, code: int):
        return self.patient_record.search_note(code)
    
    def update_note(self, code: int, text: str):
        return self.patient_record.update_note(code, text)
    
    def delete_note(self, code: int):
        return self.patient_record.delete_note(code)
        
    def retrieve_notes(self, text):
        return self.patient_record.retrieve_notes(text)
        
    def list_notes(self): 
        return self.patient_record.list_notes()
