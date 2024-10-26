from .notes import Note
class PatientRecord():
    def __init__(self):
        self.notecounter = 0
        self.note_list = []

    def add_note(self, note_details):
        if note_details != None:
            self.notecounter += 1
            new_note = Note(self.notecounter, note_details)
            self.note_list.append(new_note)
            return new_note
        return None
    def find_note(self, notecode):
        if notecode > 0:
            for i in range(self.notecounter):
                note = self.note_list[i]
                if note.code == notecode:
                    return note
        return None
