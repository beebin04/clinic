from datetime import date
class Note:
    def __init__(self, code=0, text="null", timestamp=date.today()):
        self.code = code
        self.text = text
        self.timestamp = timestamp
    def __eq__(self, other):
        if self.text == other.text and self.code == other.code:
            return True
        return False
