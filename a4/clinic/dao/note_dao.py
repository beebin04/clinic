from abc import ABC, abstractmethod
class NoteDAO(ABC):
    @abstractmethod
    #deffers to NoteDaoPickle, which searches for a note with a key and returns it
    def search_note(self, key):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle, which creates a new note containing the input as text and returns it
    def create_note(self, text):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle, which searches for any notes containing the input string and returns them as a list
    def retrieve_notes(self, search_string):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle, searches for a note with the key and updates the text
    def update_note(self, key, text):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle, which searches for a note by the key and deletes it
    def delete_note(self, key):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle, which returns a list of all notes in the record
    def list_notes(self):
        pass
