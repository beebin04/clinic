from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
class DeleteNoteWidget(QDialog):
    def __init__(self, main_window, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Delete Note")
        
        layout = QGridLayout()
        
        self.search_code_label = QLabel("Search Code:")
        self.search_code_field = QLineEdit(self)
        self.delete_button = QPushButton("Remove")
        layout.addWidget(self.search_code_label, 0, 0)
        layout.addWidget(self.search_code_field, 0, 1)
        layout.addWidget(self.delete_button, 0, 2)
        
        self.setLayout(layout)
        self.delete_button.clicked.connect(self.delete)
        
        if main_window.selected_note.text() != "":
            self.search_code_field.setText(main_window.selected_note.text())
    def delete(self):
        try:
            code = int(self.search_code_field.text())
            if self.controller.delete_note(code):
                QMessageBox.information(self, "Success", "Note Deleted")
                self.accept()
            else:
                QMessageBox.warning(self, "Error", f"Could not find note with code {code}")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", f"Code {code} is not in valid format, please use integers only")
        