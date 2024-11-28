from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QTableView, QVBoxLayout
from PyQt6.QtGui import QStandardItemModel, QStandardItem
class ListPatientWidget(QWidget):
    patient_selected = pyqtSignal(dict)
    def __init__(self, controller): 
        super().__init__() 
        self.controller = controller 
        self.table_view = QTableView() 
        self.main_layout = QVBoxLayout() 
        self.load_patients() 
        self.main_layout.addWidget(self.table_view) 
        self.setLayout(self.main_layout) 
        self.table_view.clicked.connect(self.on_patient_selected)
    def load_patients(self): 
        patients = self.controller.list_patients() 
        li = [pat.to_dict() for pat in patients] 
        self.model = QStandardItemModel(len(li), 6) 
        self.model.setHorizontalHeaderLabels([
            "PHN", 
            "Name", 
            "Birth Date", 
            "Phone Num.", 
            "Email", 
            "Address"
            ]) 
        for row, patient in enumerate(li): 
            self.model.setItem(row, 0, QStandardItem(str(patient["phn"]))) 
            self.model.setItem(row, 1, QStandardItem(patient["name"])) 
            self.model.setItem(row, 2, QStandardItem(patient["birth_date"])) 
            self.model.setItem(row, 3, QStandardItem(patient["phone"])) 
            self.model.setItem(row, 4, QStandardItem(patient["email"])) 
            self.model.setItem(row, 5, QStandardItem(patient["address"])) 
        
        self.table_view.setModel(self.model)
        self.table_view.resizeColumnsToContents()
        if hasattr(self.parentWidget(), 'update_patient_count'): 
            self.parentWidget().update_patient_count(len(li))
    def on_patient_selected(self, index):
        selected_row = index.row() 
        patient = { 
                   "phn": self.model.item(selected_row, 0).text(), 
                   "name": self.model.item(selected_row, 1).text(), 
                   "birth_date": self.model.item(selected_row, 2).text(), 
                   "phone": self.model.item(selected_row, 3).text(), 
                   "email": self.model.item(selected_row, 4).text(), 
                   "address": self.model.item(selected_row, 5).text()
                   }
        self.patient_selected.emit(patient)
    def get_num_patients(self):
        return self.model.rowCount() if self.model else 0