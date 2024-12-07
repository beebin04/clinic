from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from clinic.exception.illegal_operation_exception import IllegalOperationException
class DeletePatientWidget(QDialog):
    def __init__(self, main_window, controller):
        super().__init__()
        self.setWindowTitle("Delete Patient")
        self.controller = controller
        
        layout = QGridLayout()
        
        self.search_phn_label = QLabel("Search PHN:")
        self.search_phn_field = QLineEdit(self)
        self.delete_button = QPushButton("Remove")        
        layout.addWidget(self.search_phn_label, 0, 0)
        layout.addWidget(self.search_phn_field, 0, 1)
        layout.addWidget(self.delete_button, 0, 2)
        
        self.setLayout(layout)
        self.delete_button.clicked.connect(self.delete_patient)
        
        if main_window.current_patient_field.text() != "":
            self.search_phn_field.setText(main_window.current_patient_field.text())
        
    def delete_patient(self):
        try:
            self.controller.unset_current_patient()
            phn = int(self.search_phn_field.text())
            if self.controller.delete_patient(phn):
                QMessageBox.information(self, "Success", "Patient removed from system")
                self.accept()
            else:
                QMessageBox.warning(self, "Error", f"Patient with PHN:{phn} not found")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", f"PHN not in valid format; please use integers")
        except IllegalOperationException:
            failedDialog = QMessageBox(self)
            failedDialog.setIcon(QMessageBox.Icon.Critical)
            failedDialog.setWindowTitle("Delete Failed")
            failedDialog.setText("This PHN has no associated patient")
            failedDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
            failedDialog.exec()