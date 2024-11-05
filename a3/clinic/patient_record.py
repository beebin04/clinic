from .notes import Note
class PatientRecord():
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
    
    def create_note(self, note_details: str = None):
        if note_details != None:
            self.notecounter += 1
            new_note = Note(self.notecounter, note_details)
            self.note_list.append(new_note)
            return new_note
        return None
    
    def search_note(self, notecode: int) -> Note:
        if notecode > 0:
            for i in range(self.notecounter):
                note = self.note_list[i]
                if note.code == notecode:
                    return note
        return None
    
    def update_note(self, code: int, details: str):
        note = self.search_note(code)
        if note is not None:
            note.update(details)
            return True
        return False
    
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
        
    def retrieve_notes(self, text):
        li = []
        for note in self.note_list:
            if text in note.text:
                li.append(note)
        if len(li) != 0:
            return li
        else:
            return None
        
