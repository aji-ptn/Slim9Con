import serial
from PyQt5 import QtWidgets

class ThreadAxisAPI:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.ser = serial.Serial(self.serial_port, 9600, timeout=0.5)

    def axis_init(self):
        self.ser.write(str.encode('H \r\n'))
        print("BACK to init position: 0 mm")

    def reset(self):
    #     self.ser.write(str.encode('RESET \r\n'))
        print("SYSTEM RESET")
        self.absolute_moving(0)
        self.default_speed()

    def absolute_moving(self, distance):
        self.ser.write(str.encode('MA ' + str(distance) + '\r\n'))
        print("Absolute_moving:" + str(distance) + "mm")

    def related_moving(self, distance):
        self.ser.write(str.encode('MR ' + str(distance) + '\r\n'))
        print("Related_moving:" + str(distance) + "mm")

    def default_speed(self):
        self.ser.write(str.encode('VM=500 \r\n'))
        print("speed:500RPS")

    def set_speed(self, speed):
        self.ser.write(str.encode('VM=' + str(speed) + '\r\n'))
        print("speed:" + str(speed) + "RPS")

    def show_position(self):
        self.ser.write(str.encode('?PC \r\n'))
        self.read_position()

    def set_serial_port(self, serial_port):
        self.serial_port = serial_port

    def connect_serial(self):
        self.ser = serial.Serial(self.serial_port, 9600, timeout=0.5)
        print("SYSTEM CONNECTED")

    def disconnect_serial(self):
        self.ser.close()
        print("SYSTEM DISCONNECTED")

    def read_position(self):
        data = self.ser.read(1024)
        data_str = data.decode(encoding='UTF-8')
        data_split = data_str.split('\r\n')
        print('Current Position: ' + str(data_split[-2]) + " mm")
        QtWidgets.QMessageBox.about(None, "Information", "current Position " + str(data_split[-2]) + " mm")