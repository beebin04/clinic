from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from clinic.controller import Controller
from .create_patient_gui import CreatePatientWidget
from .search_patient_gui import SearchPatientWidget
from .retrieve_patients_gui import RetrievePatientsWidget
from .update_patient_gui import UpdatePatientWidget
from .delete_patient_gui import DeletePatientWidget
from .list_patients_gui import ListPatientWidget
from .appointment_gui import AppointmentWindow
class MainMenuGui(QMainWindow):
    def __init__(self, parent_gui, controller):
        super().__init__()
        self.controller = controller
        self.parent_gui = parent_gui
        self.setWindowTitle("Medical Clinic System")
        central_widget = QWidget()
        main_layout = QGridLayout(central_widget)
        
        #Patient options and operations section
        options_layout = QVBoxLayout()
        self.add_button = QPushButton("Add Patient")
        options_layout.addWidget(self.add_button)
        self.search_button = QPushButton("Search Patient")
        options_layout.addWidget(self.search_button)
        self.update_button = QPushButton("Update Patient")
        options_layout.addWidget(self.update_button)
        self.delete_button = QPushButton("Delete Patient")
        options_layout.addWidget(self.delete_button)
        self.retrieve_button = QPushButton("Retrieve Patients")
        options_layout.addWidget(self.retrieve_button)
        self.appt_button = QPushButton("Start Appointment")
        options_layout.addWidget(self.appt_button)
        
        
        
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        options_layout.addWidget(self.logout_button)
        
        options_widget = QWidget()
        options_widget.setLayout(options_layout)
        
        main_layout.addWidget(options_widget, 1, 0)
        
        #data section (current patient, num patients)
        data_layout = QHBoxLayout()
        data_widget = QWidget()
        self.current_patient_label = QLabel("Selected Patient:")
        self.current_patient_field = QLabel("")
        
        self.num_patients_label = QLabel("Number of Patients in System:")
        self.num_patients_field = QLabel("")
        
        data_layout.addWidget(self.num_patients_label, 0)
        data_layout.addWidget(self.num_patients_field, 1)        
        data_layout.addWidget(self.current_patient_label, 2)
        data_layout.addWidget(self.current_patient_field, 3)

        data_widget.setLayout(data_layout)
        
        main_layout.addWidget(data_widget, 0, 0, 1, 0)
        self.update_button.clicked.connect(self.update_patient)
        self.search_button.clicked.connect(self.search_patient)
        self.add_button.clicked.connect(self.create_patient)
        self.delete_button.clicked.connect(self.delete_patient)
        self.retrieve_button.clicked.connect(self.retrieve_patients)
        self.appt_button.clicked.connect(self.start_appt)
        
        self.patients_window = ListPatientWidget(self.controller)
        self.patients_window.patient_selected.connect(self.update_current_patient)
        main_layout.addWidget(self.patients_window, 1, 1)
        
        self.update_patient_count(self.patients_window.get_num_patients())
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.resize(875, 300)
        
    def create_patient(self):
        patient_creator = CreatePatientWidget(self.controller)
        if patient_creator.exec():
            self.patients_window.load_patients()
            self.update_patient_count(self.patients_window.get_num_patients())
    def search_patient(self):
        patient_search = SearchPatientWidget(self.controller)
        patient_search.exec()
    def retrieve_patients(self):
        retrieve_patients = RetrievePatientsWidget(self.controller)
        retrieve_patients.exec()
    def update_patient(self):
        update_patient = UpdatePatientWidget(self, self.controller)
        if update_patient.exec():
            self.patients_window.load_patients()
    def delete_patient(self):
        delete_patient = DeletePatientWidget(self, self.controller)
        if delete_patient.exec():
            self.patients_window.load_patients()
            self.update_patient_count(self.patients_window.get_num_patients())
    def start_appt(self):
        if not self.controller.current_patient:
            QMessageBox.critical(self, "Error", "No Patient Currently Selected")
        start_appt = AppointmentWindow(self, self.controller)
        start_appt.exec()
    def update_current_patient(self, patient):
        self.current_patient_field.setText(patient["phn"])
        self.controller.set_current_patient(int(patient["phn"]))
    def update_patient_count(self, count): 
        self.num_patients_field.setText(str(count))
    def logout(self):
        self.controller.logout()
        self.hide()
        self.parent_gui.show()
        
    