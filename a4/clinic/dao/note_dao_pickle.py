from note_dao import NoteDAO
from pickle import load, dump
class NoteDAOPickle(NoteDAO):
    
    def __init__(self, autosave=False):
        self.autosave = autosave
        self.filename = 'clinic/records/notes.dat'
        if self.autosave:
            try:
                with open(self.filename, 'rb') as file:
                    self.note_record = load(file)
            except FileNotFoundError:
                self.note_record = []
        else:
            self.note_record = []
            
    def search_note(self, key):
        pass

    def create_note(self, text):
        pass

    def retrieve_notes(self, search_string):
        pass

    def update_note(self, key, text):
        pass

    def delete_note(self, key):
        pass

    def list_notes(self):
        pass