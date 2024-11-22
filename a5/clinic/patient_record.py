from .note import Note
from .dao.note_dao_pickle import NoteDAOPickle

class PatientRecord:

    #initialization block
    def __init__(self, phn = None, autosave=False):
        self.note_dao = NoteDAOPickle(phn, autosave)
        
    def __eq__(self, other):
        if self.note_dao.notecounter == other.note_dao.notecounter:
            i = 0
            for note in self.note_dao.note_record:
                if note != other.note_dao.note_record[i]:
                    return False
            return True
        return False
    
    #creates a new note for the current patient's patient record, gives the note a code by incrementing a counter in patient record
    def create_note(self, note_details: str = None):
        return self.note_dao.create_note(note_details)
        
   #searches for a note by note code    
    def search_note(self, notecode: int) -> Note:
        return self.note_dao.search_note(notecode)
        
   #updates the text body of a note        
    def update_note(self, code: int, details: str):
        return self.note_dao.update_note(code, details)
        
    #selects a note by code and deletes it    
    def delete_note(self, code: int):
        return self.note_dao.delete_note(code)
    
    def list_notes(self):
        return self.note_dao.list_notes()
        
    #searches for all notes containing the given text and returns them as a list                    
    def retrieve_notes(self, text):
        return self.note_dao.retrieve_notes(text)

        
