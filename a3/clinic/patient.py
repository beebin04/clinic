import patient_record
class Patient():


    def __init__(self, phn=0, n="null", b="null", p="null", e="null", a="null"):
        self.phn = phn
        self.name = n
        self.birth_date = b
        self.phone = p
        self.email = e
        self.address = a
        self.patient_record
    def __repr__(self):
        return "Patient(%d, %s, %s, %s, %s, %s)" % (self.phn, self.name, self.birth_date, self.phone, self.email, self.address)
    def __eq__(self, other):
        if self.phn != other.phn:
            return False
        if self.name != other.name:
            return False
        if self.birth_date != other.birth_date:
            return False
        if self.phone != other.phone:
            return False
        if self.email != other.email:
            return False
        if self.address != other.address:
            return False
        return True