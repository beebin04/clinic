from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout
class UpdateNoteWidget(QDialog):
    def __init__(self, main_window, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Update Note")
        main_layout = QVBoxLayout()
        
        search_group = QGroupBox("Search")
        search_layout = QHBoxLayout()
        
        search_label = QLabel("Search Code:")
        self.search_field = QLineEdit()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)
        
        search_group.setLayout(search_layout)
        
        note_text_label = QLabel("Note Details:")
        self.note_text = QLineEdit()
        
        note_date_label = QLabel("Note Timestamp")
        self.note_date = QLineEdit()
        self.note_date.setEnabled(False)
        
        self.update_note = QPushButton("Update")
        self.update_note.clicked.connect(self.update)
        self.update_note.setEnabled(False)
                
        details_group = QGroupBox("Note Details")
        details_layout = QGridLayout()
        
        
        details_layout.addWidget(note_text_label, 0, 0)
        details_layout.addWidget(self.note_text, 0, 1)
        details_layout.addWidget(note_date_label, 1, 0)
        details_layout.addWidget(self.note_date, 1, 1)
        details_layout.addWidget(self.update_note, 2, 0)
        
        details_group.setLayout(details_layout)
        
        main_layout.addWidget(search_group)
        main_layout.addWidget(details_group)
        
        self.setLayout(main_layout)
        
        self.note_text.textChanged.connect(self.enable_update)
        if main_window.selected_note.text() != "":
            self.search_field.setText(main_window.selected_note.text())
        
    def search(self):
        code = self.search_field.text().strip()
        if not code.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid code")
        code = int(code)
        try:
            note = self.controller.current_patient.search_note(code)
            if note:
                self.note_text.setText(note.text)
                self.note_date.setText(str(note.timestamp))
            else:
                QMessageBox.warning(self, "Error", f"Could not find note with code {code}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not find note with code {code}, encounterd exception {str(e)}")
    def update(self):
        try:
            code = int(self.search_field.text())
            text = self.note_text.text()
            self.controller.current_patient.update_note(code, text)  
            self.update_note.setEnabled(False)
            QMessageBox.information(self, "Success", "Note description updated")
            self.accept()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to update note: {str(e)}")        
    def enable_update(self):
        self.update_note.setEnabled(True)
    