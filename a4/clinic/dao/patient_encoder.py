from json import JSONEncoder
from typing import Any
from clinic.patient import Patient

class PatientEncoder(JSONEncoder):
    def default(self, o: Any):
        if isinstance(o, Patient):
            return {
                "__type__" : "Patient",
                "phn" : o.phn,
                "name" : o.name,
                "birth_date" : o.birth_date,
                "phone" : o.phone,
                "email" : o.email,
                "address" : o.address
            }
        return super().default(o)
