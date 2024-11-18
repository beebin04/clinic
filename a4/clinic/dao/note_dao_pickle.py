from .note_dao import NoteDAO
from pickle import load, dump
from clinic.note import Note
class NoteDAOPickle(NoteDAO):
    
    def __init__(self, phn : int = None, autosave=False):
        self.autosave = autosave
        self.filename : str = f'clinic/records/{phn}.dat'
        self.notecounter = 0
        self.note_record = []
        if self.autosave:
            try:
                with open(self.filename, 'rb') as file:
                    note_data = load(file)
                    for data in note_data:
                        self.note_record.append(Note.from_dict(data))
                    self.notecounter = len(self.note_record)
            except FileNotFoundError:
                self.note_record = []
        else:
            self.note_record = []
            
    def search_note(self, key) -> Note:
        if key > 0:
            for n in self.note_record:
                if n.code == key:
                    return n
        
    def create_note(self, text):
        if text != None:
            self.notecounter += 1
            new_note = Note(self.notecounter, text)
            self.note_record.append(new_note)
            if self.autosave:
                with open(self.filename, "wb") as file:
                    dump([n.to_dict() for n in self.note_record], file)
            return new_note
        return None

    def retrieve_notes(self, search_string):
        li = []
        for note in self.note_record:
            if search_string in note.text:
                li.append(note)
        return li

    def update_note(self, key, text):
        note = self.search_note(key)
        if note:
            note.update(text)
            if self.autosave:
                with open(self.filename, 'wb') as file:
                    dump([n.to_dict() for n in self.note_record], file)
            return True
        return False

    def delete_note(self, key):
        note = self.search_note(key)
        if note:
            self.note_record.remove(note)
            self.notecounter -= 1
            if self.autosave:
                with open(self.filename, 'wb') as file:
                    dump([n.to_dict() for n in self.note_record], file)
            return True
        return False

    def list_notes(self) -> list:
        li = []
        for note in self.note_record:
            li.insert(0, note)
        return li