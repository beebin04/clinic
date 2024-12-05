from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QDialog
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class RetrieveNotesWidget(QDialog):
	def __init__(self, controller):
		super().__init__()
		self.controller = controller
		self.setWindowTitle("Retrieve Notes By Content")
		self.main_layout = QVBoxLayout(self)

		search_group = QGroupBox("Search")
		search_layout = QHBoxLayout()

		self.search_label = QLabel("Search For Text")
		self.search_note_field = QLineEdit(self)
		self.search_button = QPushButton("Search")
		self.search_button.clicked.connect(self.retrieve_notes)

		search_layout.addWidget(self.search_label)
		search_layout.addWidget(self.search_note_field)
		search_layout.addWidget(self.search_button)

		search_group.setLayout(search_layout)
		self.main_layout.addWidget(search_group)
		self.setLayout(self.main_layout)

	def retrieve_notes(self):
		if hasattr(self, "table_view"):
			self.main_layout.removeWidget(self.table_view)
			self.table_view.deleteLater()
			self.table_view = None
		self.table_view = QTableView()
		notes = self.controller.retrieve_notes(self.search_note_field.text())
		li = []
		for note in notes:
			li.append(note.to_dict())
		self.model = QStandardItemModel(len(li), 3)
		self.model.setHorizontalHeaderLabels(["Code", "Details", "Date"])
		for row, note in enumerate(li):
			self.model.setItem(row, 0, QStandardItem(str(note["code"])))
			self.model.setItem(row, 1, QStandardItem(note["text"]))
			self.model.setItem(row, 2, QStandardItem(str(note["timestamp"])))
		self.table_view.resizeColumnsToContents()
		self.resize(637, 300)
		self.table_view.setModel(self.model)
		self.main_layout.addWidget(self.table_view)
			