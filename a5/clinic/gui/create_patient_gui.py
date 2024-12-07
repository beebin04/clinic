from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox
class CreatePatientWidget(QDialog):
    def __init__(self,  controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Add New Patient")
        layout = QFormLayout()

        self.phn_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.birth_date_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.address_input = QLineEdit(self)

        layout.addRow("PHN:", self.phn_input)
        layout.addRow("Full Name:", self.name_input)
        layout.addRow("Birth Date:", self.birth_date_input)
        layout.addRow("Phone Number:", self.phone_input)
        layout.addRow("Email:", self.email_input)
        layout.addRow("Address:", self.address_input)

        add_button = QPushButton("Add Patient")
        add_button.clicked.connect(self.add_patient)

        layout.addWidget(add_button)
        self.resize(300, 150)
        self.setLayout(layout)
    def add_patient(self):
        try:
            phn = int(self.phn_input.text())
            name = self.name_input.text()
            bd = self.birth_date_input.text()
            phone = self.phone_input.text()
            em = self.email_input.text()
            addy = self.address_input.text()
            self.controller.create_patient(phn, name, bd, phone, em, addy)
            QMessageBox.information(self, "Success", "Patient added to system")
            self.accept()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error adding patient")