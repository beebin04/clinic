from datetime import date
class Note:
    #initialization block
    def __init__(self, code: int, text: str, timestamp=date.today()):
        self.code = code
        self.text = text
        self.timestamp = timestamp
        
    #equals operator    
    def __eq__(self, other):
        if self.text == other.text and self.code == other.code:
            return True
        return False
        
    #returns the representation of the Note 
    def __repr__(self) -> str:
        return "Note(%d, %s, %r)" % (self.code, self.text, self.timestamp)
        
    #returns the string representation of the note
    def __str__(self):
        return "Code: " + str(self.code) + " Description: " + self.text + " Date: " + str(self.timestamp)
    def to_dict(self) -> dict:
        return {
            "__type__" : 'Note', 
            "code" : self.code, 
            "text" : self.text,
            "timestamp" : self.timestamp
            }
    @classmethod
    def from_dict(cls, data:dict):
        if '__type__' in data and data['__type__'] == 'Note':
            return cls(data["code"], data["text"], data["timestamp"])
        
    
    #updates the text body of the note
    def update(self, new_txt: str):
        self.text = new_txt
        
