from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QWidget
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTableView, QDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem
class RetrievePatientsWindow(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Retrieve Patient By Name")
        self.main_layout = QVBoxLayout(self)
        
        search_group = QGroupBox("Search")
        search_layout = QHBoxLayout()
        
        self.search_label = QLabel("Search For Name")
        self.search_name_field = QLineEdit(self)
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.retrieve_patients)
        
        
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_name_field)
        search_layout.addWidget(self.search_button)
        
        search_group.setLayout(search_layout)
        self.main_layout.addWidget(search_group)
        self.setLayout(self.main_layout)
    def retrieve_patients(self):
        if hasattr(self, "table_view"):
            self.main_layout.removeWidget(self.table_view)
            self.table_view.deleteLater()
            self.table_view = None
        self.table_view = QTableView()
        patients = self.controller.retrieve_patients(self.search_name_field.text())
        li = []
        for pat in patients:
            li.append(pat.to_dict())
        self.model = QStandardItemModel(len(li), 6)
        self.model.setHorizontalHeaderLabels(["PHN", "Name", "Birth Date", "Phone Num.", "Email", "Address"])
        for row, patient in enumerate(li): 
            self.model.setItem(row, 0, QStandardItem(str(patient["phn"]))) 
            self.model.setItem(row, 1, QStandardItem(patient["name"])) 
            self.model.setItem(row, 2, QStandardItem(patient["birth_date"])) 
            self.model.setItem(row, 3, QStandardItem(patient["phone"])) 
            self.model.setItem(row, 4, QStandardItem(patient["email"])) 
            self.model.setItem(row, 5, QStandardItem(patient["address"]))
        self.table_view.resizeColumnsToContents()
        self.resize(637, 300)
        self.table_view.setModel(self.model)
        self.main_layout.addWidget(self.table_view)