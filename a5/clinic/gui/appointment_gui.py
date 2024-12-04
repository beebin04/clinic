from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QWidget, QLabel, QGridLayout, QVBoxLayout
from PyQt6.QtWidgets import QPushButton, QHBoxLayout
from .list_notes_gui import ListNotesWidget
from .create_note_gui import CreateNoteWidget
from .search_note_gui import SearchNoteWidget
from .update_note_gui import UpdateNoteWidget
from .delete_note_gui import DeleteNoteWidget

class AppointmentWindow(QDialog):
    def __init__(self, main_window, controller):
        super().__init__()
        self.setWindowTitle("Appointment Window")
        self.controller = controller
        main_layout = QGridLayout()
        
        data_layout = QHBoxLayout()
        self.label = QLabel("Now seeing:")
        self.patient = QLabel(f"{main_window.controller.current_patient.phn}, {main_window.controller.current_patient.name}")
        self.num_notes_label = QLabel("Total Notes:")
        self.num_notes = QLabel("")
        self.selected_note_label = QLabel("Selcted Note:")
        self.selected_note = QLabel("")
        data_layout.addWidget(self.label)
        data_layout.addWidget(self.patient)
        data_layout.addWidget(self.num_notes_label)
        data_layout.addWidget(self.num_notes)
        data_layout.addWidget(self.selected_note_label)
        data_layout.addWidget(self.selected_note)
        
        data_widget = QWidget()
        data_widget.setLayout(data_layout)
        main_layout.addWidget(data_widget, 0, 0, 1, 0)       
        
        options_layout = QVBoxLayout()
        self.add_note = QPushButton("Add Note")
        self.add_note.clicked.connect(self.create_note)
        options_layout.addWidget(self.add_note)
        self.search_button = QPushButton("Search Note")
        self.search_button.clicked.connect(self.search_note)
        options_layout.addWidget(self.search_button)
        self.update_button = QPushButton("Update Note")
        self.update_button.clicked.connect(self.update_note)
        options_layout.addWidget(self.update_button)
        self.delete_button = QPushButton("Delete Note")
        self.delete_button.clicked.connect(self.delete_note)
        options_layout.addWidget(self.delete_button)
        self.retrieve_button = QPushButton("Retrieve Notes")
        self.retrieve_button.clicked.connect(self.retrieve_notes)
        options_layout.addWidget(self.retrieve_button)
        self.end_appt_button = QPushButton("Close Appointment")
        self.end_appt_button.clicked.connect(self.exit)
        options_layout.addWidget(self.end_appt_button)
        
        options_widget = QWidget()
        options_widget.setLayout(options_layout)
        main_layout.addWidget(options_widget, 1, 0)
        
        self.notes_list = ListNotesWidget(self.controller)
        
        self.notes_list.note_selected.connect(self.update_current_code)
        
        main_layout.addWidget(self.notes_list, 1, 1)
        self.update_note_count(self.notes_list.get_num_notes())
        self.setLayout(main_layout)
        self.resize(535, 150)
        
    def create_note(self):
        note_creator = CreateNoteWidget(self.controller)
        if note_creator.exec():
            self.notes_list.load_notes()
            self.update_note_count(self.notes_list.get_num_notes())
    def search_note(self):
        note_search = SearchNoteWidget(self.controller)
        note_search.exec()
    def update_note(self):
        note_update = UpdateNoteWidget(self, 
                                       self.controller)
        if note_update.exec():
            self.notes_list.load_notes()
    def delete_note(self):
        note_delete = DeleteNoteWidget(self, self.controller)
        if note_delete.exec():
            self.notes_list.load_notes()
            self.update_note_count(self.notes_list.get_num_notes())
    def retrieve_notes(self):
        pass
    def exit(self):
        self.close()
    def update_note_count(self, count):
        self.num_notes.setText(str(count))
    def update_current_code(self, note):
        self.selected_note.setText(note["code"])