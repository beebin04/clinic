from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
class ListNotesWidget(QWidget):
    
    note_selected = pyqtSignal(dict)
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.table_view = QTableView()
        main_layout = QVBoxLayout()
        self.load_notes()
        main_layout.addWidget(self.table_view)
        self.setLayout(main_layout)
        self.table_view.clicked.connect(self.on_note_selected)
        
        
    def load_notes(self):
        notes = self.controller.current_patient.list_notes()
        li = [note.to_dict() for note in notes]
        
        self.model = QStandardItemModel(len(li), 3)
        self.model.setHorizontalHeaderLabels([
            "Code",
            "Details",
            "Date"
        ])
        
        for row, note in enumerate(li):
            
            self.model.setItem(row, 0, QStandardItem(str(note["code"])))
            self.model.setItem(row, 1, QStandardItem(note["text"]))
            self.model.setItem(row, 2, QStandardItem(str(note["timestamp"])))
        
        self.table_view.setModel(self.model)
        self.table_view.resizeColumnsToContents()
        if hasattr(self.parentWidget(), 'update_note_count'):
            self.parentWidget().update_note_count(len(li))
            
    def on_note_selected(self, index):
        selected_row = index.row()
        
        note = {
            "code" : self.model.item(selected_row, 0).text(),
            "text" : self.model.item(selected_row, 1).text(),
            "timestamp" : self.model.item(selected_row, 2).text()   
        }
        
        self.note_selected.emit(note)
        
    def get_num_notes(self):
        return self.model.rowCount() if self.model else 0