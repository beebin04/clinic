from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog
class UpdatePatientWindow(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Update Patient")