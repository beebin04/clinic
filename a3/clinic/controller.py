from .patient import Patient
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
    def retrieve_patients(self, name):
        if self.usrlogin:
            result = []
            for patient in self.patient_list:
                if name in patient.name:
                    result.append(patient)
            return result
        else:
            return None
    def update_patient(self, searchphn, phn, name, bd, phone, email, address):
        if self.usrlogin:
            if self.search_patient(phn) != None and searchphn != phn:
                return False
            pat = self.search_patient(searchphn)
            if pat != None:
                pat.phn = phn
                pat.name = name
                pat.birth_date = bd
                pat.phone = phone
                pat.email = email
                pat.address = address
                return True
        else:
            return False
        