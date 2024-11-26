from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog
class DeletePatientWindow(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Delete Patient")
        self.controller = controller
        