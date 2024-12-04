from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout
class SearchPatientWidget(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Search Patient")
        self.controller = controller
        
        main_layout = QVBoxLayout(self)
        
        search_group = QGroupBox("Search") 
        search_layout = QGridLayout() 
        
        self.label_search_phn = QLabel("Search PHN:") 
        self.search_field = QLineEdit(self) 
        self.search_field.setMaximumWidth(150)
        self.search_button = QPushButton("Search") 
        self.search_button.clicked.connect(self.search_patient) 
        
        search_layout.addWidget(self.label_search_phn, 0, 0) 
        search_layout.addWidget(self.search_field, 0, 1) 
        search_layout.addWidget(self.search_button, 0, 2) 
        
        
        search_group.setLayout(search_layout) 
        
        details_group = QGroupBox("Patient Details") 
        details_layout = QGridLayout() 
        
        self.label_patient_phn = QLabel("PHN:") 
        self.phn_field = QLabel("")
         
        self.label_patient_name = QLabel("Name:") 
        self.name_field = QLabel("") 
        
        self.label_patient_birth_day = QLabel("Birth Date (YYYY-MM-DD):") 
        self.bd_field = QLabel("")
        
        self.label_patient_phone = QLabel("Phone Number:") 
        self.phone_field = QLabel("")
        
        self.label_patient_email = QLabel("Email Address:") 
        self.email_field = QLabel("")
        
        self.label_patient_address = QLabel("Address:") 
        self.address_field = QLabel("")
        
        for field in [self.phn_field, self.name_field, self.bd_field, self.phone_field, self.email_field, self.address_field]: 
            field.setMinimumWidth(200)
            
        details_layout.addWidget(self.label_patient_phn, 0, 0) 
        details_layout.addWidget(self.phn_field, 0, 1) 
        details_layout.addWidget(self.label_patient_name, 1, 0) 
        details_layout.addWidget(self.name_field, 1, 1) 
        details_layout.addWidget(self.label_patient_birth_day, 2, 0)
        details_layout.addWidget(self.bd_field, 2, 1)
        details_layout.addWidget(self.label_patient_phone, 3, 0)
        details_layout.addWidget(self.phone_field, 3, 1)
        details_layout.addWidget(self.label_patient_email, 4, 0)
        details_layout.addWidget(self.email_field, 4, 1)
        details_layout.addWidget(self.label_patient_address, 5, 0) 
        details_layout.addWidget(self.address_field, 5, 1)
        
        details_group.setLayout(details_layout)
        
        main_layout.addWidget(search_group)
        main_layout.addWidget(details_group)
        
    def search_patient(self):
        search_phn = self.search_field.text().strip()
        if not search_phn.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN")
            return
        search_phn = int(search_phn)
        try:
            patient = self.controller.search_patient(search_phn)
            if patient:
                self.name_field.setText(str(patient.name))
                self.phn_field.setText(str(patient.phn))
                self.bd_field.setText(str(patient.birth_date))
                self.phone_field.setText(str(patient.phone))
                self.email_field.setText(str(patient.email))
                self.address_field.setText(str(patient.address))
            else:
                QMessageBox.warning(self, "Patient Not Found", f"Patient with PHN:{str(search_phn)} could not be found")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error finding patient: {str(e)}")