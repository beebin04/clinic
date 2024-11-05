from .notes import Note
class PatientRecord():

    #initialization block
    def __init__(self):
        self.notecounter = 0
        self.note_list = []
        
    def __eq__(self, other):
        if self.notecounter == other.notecounter:
            i = 0
            for note in self.note_list:
                if note != other.note_list[i]:
                    return False
            return True
        return False
    
    #creates a new note for the current patient's patient record, gives the note a code by incrementing a counter in patient record
    def create_note(self, note_details: str = None):
        if note_details != None:
            self.notecounter += 1
            new_note = Note(self.notecounter, note_details)
            self.note_list.append(new_note)
            return new_note
        return None
        
   #searches for a note by note code    
    def search_note(self, notecode: int) -> Note:
        if notecode > 0:
            for i in range(self.notecounter):
                note = self.note_list[i]
                if note.code == notecode:
                    return note
        return None
        
   #updates the text body of a note        
    def update_note(self, code: int, details: str):
        note = self.search_note(code)
        if note is not None:
            note.update(details)
            return True
        return False
        
    #selects a note by code and deletes it    
    def delete_note(self, code: int):
        note = self.search_note(code)
        if note is not None:
            self.note_list.remove(note)
            self.notecounter -= 1
            return True
        return False
    
    def list_notes(self):
        li = []
        for n in self.note_list:
            li.insert(0, n)
        if len(li) > 0:
            return li
        else:
            return None
        
    #searches for all notes containing the given text and returns them as a list                    
    def retrieve_notes(self, text):
        li = []
        for note in self.note_list:
            if text in note.text:
                li.append(note)
        if len(li) != 0:
            return li
        else:
            return None
        
