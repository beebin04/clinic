from datetime import date
class Note:
    #dmdeakndlsk askd akmsd; almsd
    def __init__(self, code: int, text: str):
        self.code = code
        self.text = text
        self.timestamp = date.today()
        
    def __eq__(self, other):
        if self.text == other.text and self.code == other.code:
            return True
        return False
    def __repr__(self) -> str:
        return "Note(%d, %s, %r)" % (self.code, self.text, self.timestamp)
    def __str__(self):
        return "Code: " + self.code + " Description: " + self.text + " Date: " + self.timestamp
    
    def update(self, new_txt: str):
        self.text = new_txt
    