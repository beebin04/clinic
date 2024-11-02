from .patient import Patient
class Controller:
    def __init__(self, usrlogin=False):
        self.usrlogin = usrlogin
        self.current_patient = None
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
            if pat != None and pat != self.current_patient:
                pat.phn = phn
                pat.name = name
                pat.birth_date = bd
                pat.phone = phone
                pat.email = email
                pat.address = address
                return True
        else:
            return False
    def delete_patient(self, phn):
        if self.usrlogin is False:
            return False
        patient = self.search_patient(phn)
        if patient != None and patient != self.current_patient:
            self.patient_list.remove(patient)
            return True
        else:
            return False
    def list_patients(self):
        if self.usrlogin:
            li = []
            for p in self.patient_list:
                li.append(p)
            return li
        return None
    def set_current_patient(self, phn):
        if self.usrlogin:
            p = self.search_patient(phn)
            if p is not None:
                self.current_patient = p
        return None
    def get_current_patient(self):
        if self.usrlogin:
            return self.current_patient
        return None
    def unset_current_patient(self):
        self.current_patient = None
        return
    def create_note(self, note_details=str):
        if self.usrlogin:
            if self.current_patient != None:
                new_note = self.current_patient.patient_record.add_note(note_details)
                return new_note
        return None
    def search_note(self, note_code):
        if self.usrlogin:
            if self.current_patient != None:
                note = self.current_patient.patient_record.find_note(note_code)
                return note
        return None
