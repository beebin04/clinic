from patient import Patient
class Controller:
    def __init__(self, usrlogin=False):
        self.usrlogin = usrlogin
        self.patient_list =[]
    def login(self, usr, pswd):
        if self.usrlogin == True:
            return False 
        if usr == "user" and pswd == "clinic2024":
            self.usrlogin = True
        return self.usrlogin
    
    def logout(self):
        if self.usrlogin:
            self.usrlogin = False
            return True
        else:
            return False
    def create_patient(self, phn, n, b, p, e, a):
        if self.search_patient(phn) == None:
            if self.usrlogin:
                p = Patient(phn, n, b, p, e, a)
                self.patient_list.append(p)
                return p
            else:
                return None
        else: 
            return None
    def search_patient(self, phn):
        if self.usrlogin:
            for patient in self.patient_list:
                if patient.phn == phn:
                    return patient
        return None    