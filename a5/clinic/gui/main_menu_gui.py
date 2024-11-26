from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout
from clinic.controller import Controller
from .create_patient_gui import CreatePatientWindow
from .search_patinet_gui import SearchPatientWindow
from .retrieve_patinets_gui import RetrievePatientsWindow
from .update_patient_gui import UpdatePatientWindow
from .delete_patient_gui import DeletePatientWindow
class MainMenuGui(QMainWindow):
    def __init__(self, parent_gui, controller):
        super().__init__()
        self.controller = controller
        self.parent_gui = parent_gui
        self.setWindowTitle("Medical Clinic System")
        self.resize(300, 300)
        
        self.add_patient_button = QPushButton("Add New Patient")
        self.add_patient_button.clicked.connect(self.create_patient)
        self.search_patient_button = QPushButton("Search Patient By PHN")
        self.search_patient_button.clicked.connect(self.search_patient)
        self.retrieve_patient_button = QPushButton("Retrieve Patients By Name")        
        self.retrieve_patient_button.clicked.connect(self.retrieve_patients)
        self.update_patient_button = QPushButton("Update Patient Data")
        self.update_patient_button.clicked.connect(self.update_patient)
        self.delete_patient_button = QPushButton("Delete A Patient")
        self.delete_patient_button.clicked.connect(self.delete_patient)
        self.list_patients_button = QPushButton("List All Patients")
        self.list_patients_button.clicked.connect(self.list_patients)
        self.start_appointment_button = QPushButton("Begin An Appointment")
        self.start_appointment_button.clicked.connect(self.start_appt)
        
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout = QVBoxLayout()
        layout.addWidget(self.add_patient_button)
        layout.addWidget(self.search_patient_button)
        layout.addWidget(self.retrieve_patient_button)
        layout.addWidget(self.update_patient_button)
        layout.addWidget(self.delete_patient_button)
        layout.addWidget(self.list_patients_button)
        layout.addWidget(self.start_appointment_button)
        layout.addWidget(self.logout_button)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
    def create_patient(self):
        patient_creator = CreatePatientWindow(self.controller)
        patient_creator.exec()
    def search_patient(self):
        patient_search = SearchPatientWindow(self.controller)
        patient_search.exec()
    def retrieve_patients(self):
        retrieve_patients = RetrievePatientsWindow(self.controller)
        retrieve_patients.exec()
    def update_patient(self):
        update_patient = UpdatePatientWindow(self.controller)
        update_patient.exec()
    def delete_patient(self):
        delete_patient = DeletePatientWindow(self.controller)
        delete_patient.exec()
    def list_patients(self):
        #list_patients = ListPatientsWindow(self.controller)
        #list_patients.exec()
        pass
    def start_appt(self):
        #start_appt = PatientAppointmentWindow(self.controller)
        #start_appt.exec()
        pass
    def logout(self):
        self.controller.logout()
        self.hide()
        self.parent_gui.show()
        
    