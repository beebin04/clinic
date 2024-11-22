from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout
from clinic.controller import Controller
class MainMenuGui(QMainWindow):
    def __init__(self, parent_gui, controller):
        super().__init__()
        self.controller = controller
        self.parent_gui = parent_gui
        self.parent_gui.hide()
        
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
        pass
    def search_patient(self):
        pass
    def retrieve_patients(self):
        pass
    def update_patient(self):
        pass
    def delete_patient(self):
        pass
    def list_patients(self):
        pass
    def start_appt(self):
        pass
    def logout(self):
        self.controller.logout()
        self.hide()
        self.parent_gui.show()
        
    