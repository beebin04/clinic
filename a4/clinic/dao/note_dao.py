from abc import ABC, abstractmethod
class NoteDAO(ABC):
    @abstractmethod
    #deffers to NoteDaoPickle
    def search_note(self, key):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle
    def create_note(self, text):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle
    def retrieve_notes(self, search_string):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle
    def update_note(self, key, text):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle
    def delete_note(self, key):
        pass
    @abstractmethod
    #deffers to NoteDaoPickle
    def list_notes(self):
        pass
