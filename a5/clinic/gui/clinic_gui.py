import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt6.QtWidgets import QLabel, QLineEdit, QGridLayout, QPushButton
from clinic.controller import Controller
from .main_menu_gui import MainMenuGui
from clinic.exception import *
class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.controller = Controller(autosave=True)
        self.setWindowTitle("Login")
        self.user_label = QLabel("Username:")
        self.user_field = QLineEdit()
        self.pass_label = QLabel("Password:")
        self.pass_field = QLineEdit()
        self.pass_field.setEchoMode(QLineEdit.EchoMode.Password)
        central = QWidget()
        self.setCentralWidget(central)
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        
        layout1 = QGridLayout()
        
        layout1.addWidget(self.user_label, 0, 0)
        layout1.addWidget(self.user_field, 0, 1)
        layout1.addWidget(self.pass_label, 1, 0)
        layout1.addWidget(self.pass_field, 1, 1)
        layout1.addWidget(self.login_button, 2, 0, 1, 2)
        # Continue here with your code!
        central.setLayout(layout1)
        self.setCentralWidget(central)
        
    def login(self):
        try:
            if self.controller.login(self.user_field.text(), self.pass_field.text()):
                self.hide()
                self.clinic_manager = MainMenuGui(self, self.controller)
                self.clinic_manager.show()
                self.user_field.clear()
                self.pass_field.clear()
            
        except InvalidLoginException:
            failedDialog = QMessageBox(self)
            failedDialog.setIcon(QMessageBox.Icon.Critical)
            failedDialog.setWindowTitle("Login Failed")
            failedDialog.setText("Incorrect Username or Password")
            failedDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
            failedDialog.exec()
        
        

def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
