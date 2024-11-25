from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout
class UpdatePatientWindow(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Update Patient")
        
        main_layout = QVBoxLayout(self)
        
        search_group = QGroupBox("Search")
        search_layout = QGridLayout()
        
        self.search_phn_label = QLabel("Search PHN:")
        self.search_phn_field = QLineEdit(self)
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_patient)
        
        search_layout.addWidget(self.search_phn_label, 0, 0)
        search_layout.addWidget(self.search_phn_field, 0, 1)
        search_layout.addWidget(self.search_button, 0, 2)
        
        search_group.setLayout(search_layout)
        main_layout.addWidget(search_group)
        
        data_group = QGroupBox("Data")
        data_layout = QGridLayout()
        
        self.name_label = QLabel("Full Name:")
        self.name_field = QLineEdit(self)
        data_layout.addWidget(self.name_label, 0, 0)
        data_layout.addWidget(self.name_field, 0, 1)
        
        self.patient_phn_label = QLabel("Personal Health Num.:")
        self.patient_phn_field = QLineEdit(self)
        data_layout.addWidget(self.patient_phn_label, 1, 0)
        data_layout.addWidget(self.patient_phn_field, 1, 1)
        
        self.dob_label = QLabel("Birth Date:")
        self.dob_field = QLineEdit(self)
        data_layout.addWidget(self.dob_label, 0, 2)
        data_layout.addWidget(self.dob_field, 0, 3)

        self.phone_label = QLabel("Phone #:")
        self.phone_field = QLineEdit(self)
        data_layout.addWidget(self.phone_label, 1, 2)
        data_layout.addWidget(self.phone_field, 1, 3) 
        
        self.email_label = QLabel("Email:") 
        self.email_field = QLineEdit(self)
        data_layout.addWidget(self.email_label, 0, 4)
        data_layout.addWidget(self.email_field, 0, 5)
        
        self.address_label = QLabel("Address:")
        self.address_field = QLineEdit(self)
        data_layout.addWidget(self.address_label, 1, 4)
        data_layout.addWidget(self.address_field, 1, 5)
        
        data_group.setLayout(data_layout)
        main_layout.addWidget(data_group)
        self.setLayout(main_layout)
    def search_patient(self):
        search_phn = self.search_phn_field.text().strip()
        if not search_phn.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN")
            return
        search_phn = int(search_phn)
        try:
            patient = self.controller.search_patient(search_phn)
            if patient:
                self.name_field.setText(str(patient.name))
                self.patient_phn_field.setText(str(patient.phn))
                self.dob_field.setText(str(patient.birth_date))
                self.phone_field.setText(str(patient.phone))
                self.email_field.setText(str(patient.email))
                self.address_field.setText(str(patient.address))
            else:
                QMessageBox.warning(self, "Patient Not Found", f"Patient with PHN:{str(search_phn)} could not be found")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error finding patient: {str(e)}")