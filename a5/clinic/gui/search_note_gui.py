from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
class SearchNoteWidget(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Search Note")
        main_layout = QVBoxLayout()
        
        search_group = QGroupBox("Search")
        search_layout = QHBoxLayout()
        self.controller = controller
        
        search_label = QLabel("Note Code:")
        self.search_field = QLineEdit()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_note)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)        
        
        search_group.setLayout(search_layout)
        
        details_group = QGroupBox("Note")
        details_layout = QGridLayout()
        
        self.note_text_label = QLabel("Note Details")
        self.note_text = QLabel("")
        
        self.note_date_label = QLabel("Date")
        self.note_date = QLabel("")
        
        details_layout.addWidget(self.note_text_label, 0, 0)
        details_layout.addWidget(self.note_text, 0, 1)
        details_layout.addWidget(self.note_date_label, 1, 0)
        details_layout.addWidget(self.note_date, 1, 1)
        
        details_group.setLayout(details_layout)
        
        main_layout.addWidget(search_group)
        main_layout.addWidget(details_group)
        self.setLayout(main_layout)
    def search_note(self):
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