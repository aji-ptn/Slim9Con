from UInew import Ui_MainWindow
import os
from PyQt5 import QtWidgets
from ThreadAxisAPI import ThreadAxisAPI

class Controller(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.connect_btn_event()
        self.btn_disable()

        self.position = 0
        self.speed = 500
        self.Ui.lineEdit_position.setText(str(self.position))
        self.Ui.lineEdit_speed.setText(str(self.speed))
        self.Ui.btn_home.hide()

    def connect_btn_event(self):
        self.Ui.btn_home.clicked.connect(self.go_axis_init)
        self.Ui.btn_reset.clicked.connect(self.go_reset)
        self.Ui.btn_position.clicked.connect(self.go_show_position)
        self.Ui.btn_absolute_move.clicked.connect(self.go_absolute_moving)
        self.Ui.btn_relative_move.clicked.connect(self.go_related_moving)
        self.Ui.btn_default_speed.clicked.connect(self.go_default_speed)
        self.Ui.btn_set_speed.clicked.connect(self.go_set_speed)
        self.Ui.btn_connect.clicked.connect(self.go_connect_serial)
        self.Ui.btn_disconnect.clicked.connect(self.go_disconnect_serial)
        self.Ui.btn_help.clicked.connect(self.help)

    def getPassword(self):
        paswd, ok = QtWidgets.QInputDialog.getText(None, "Authentication", "Sudo Password?",
                                                   QtWidgets.QLineEdit.Password)
        if ok and paswd != '':
            return paswd

    def btn_disable(self):
        self.Ui.btn_home.setDisabled(True)
        self.Ui.btn_reset.setDisabled(True)
        self.Ui.btn_position.setDisabled(True)
        self.Ui.btn_absolute_move.setDisabled(True)
        self.Ui.btn_relative_move.setDisabled(True)
        self.Ui.btn_default_speed.setDisabled(True)
        self.Ui.btn_set_speed.setDisabled(True)
        self.Ui.lineEdit_position.setDisabled(True)
        self.Ui.lineEdit_speed.setDisabled(True)

    def btn_enable(self):
        # self.getPassword()
        self.Ui.btn_home.setEnabled(True)
        self.Ui.btn_reset.setEnabled(True)
        self.Ui.btn_position.setEnabled(True)
        self.Ui.btn_absolute_move.setEnabled(True)
        self.Ui.btn_relative_move.setEnabled(True)
        self.Ui.btn_default_speed.setEnabled(True)
        self.Ui.btn_set_speed.setEnabled(True)
        self.Ui.lineEdit_position.setEnabled(True)
        self.Ui.lineEdit_speed.setEnabled(True)

    def go_axis_init(self):
        self.thredAxisAPI.axis_init()
        self.Ui.lineEdit_speed.text()

    def go_reset(self):
        self.position = 0
        self.speed = 500
        self.thredAxisAPI.reset()
        self.Ui.lineEdit_position.setText(" 0 ")
        self.Ui.lineEdit_speed.setText(str(self.speed))
        # self.thredAxisAPI.absolute_moving(self.position)

    def go_show_position(self):
        self.thredAxisAPI.show_position()

    def go_absolute_moving(self):
        self.position = self.Ui.lineEdit_position.text()
        self.thredAxisAPI.absolute_moving(self.position)

    def go_related_moving(self):
        self.position = self.Ui.lineEdit_position.text()
        self.thredAxisAPI.related_moving(self.position)

    def go_default_speed(self):
        self.thredAxisAPI.default_speed()

    def go_set_speed(self):
        self.speed = self.Ui.lineEdit_speed.text()
        self.thredAxisAPI.set_speed(self.speed)

    def go_connect_serial(self):
        paswd = self.getPassword()
        if paswd:
            os.system("echo "+ paswd + "| sudo -S chmod a+rw /dev/ttyUSB*")
            self.thredAxisAPI = ThreadAxisAPI(serial_port="/dev/ttyUSB0")
            self.thredAxisAPI.connect_serial()
            self.btn_enable()

    def go_disconnect_serial(self):
        self.thredAxisAPI.disconnect_serial()
        self.btn_disable()

    def help(self):
        QtWidgets.QMessageBox.about(self, "Help", "Please Contact MOIL LAB")