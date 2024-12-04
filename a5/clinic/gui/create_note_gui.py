from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QFormLayout, QPushButton, QLineEdit, QMessageBox
class CreateNoteWidget(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Create Note")
        self.controller = controller
        layout = QFormLayout()
        
        self.text_input = QLineEdit(self)
        layout.addRow("Note Details:", self.text_input)
        add_button = QPushButton("Done")
        add_button.clicked.connect(self.create_note)
        layout.addWidget(add_button)
        self.setLayout(layout)
    def create_note(self):
        text = self.text_input.text()
        if text.strip() != "":
            self.controller.current_patient.create_note(text)
            QMessageBox.information(self, "Success", "Note added to record")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Please enter details")