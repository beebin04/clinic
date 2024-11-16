from datetime import date
class Note:
    #initialization block
    def __init__(self, code: int, text: str):
        self.code = code
        self.text = text
        self.timestamp = date.today()
        
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
        return "Code: " + self.code + " Description: " + self.text + " Date: " + self.timestamp
    
    #updates the text body of the note
    def update(self, new_txt: str):
        self.text = new_txt
        
