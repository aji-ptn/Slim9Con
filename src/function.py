import serial


class Function():

    def __init__(self):
        self.ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)
        self.counter = 0

    def home(self):
        self.ser.write(str.encode('H\r\n'))
        self.counter = 0
        print("position:" + str(self.counter) + "mm")

    def reset(self):
        self.ser.write(str.encode('RESET\r\n'))
        print("SYSTEM RESET")

    def origin(self):
        self.ser.write(str.encode('MA 0'))
        self.ser.write(str.encode('\r\n'))
        self.counter = 0
        print("BACK ORIGIN")
        print("position:" + str(self.counter) + "mm")

    def show_position(self):
        print("position:" + str(self.counter) + "mm")

    def forward(self, distance):
        self.ser.write(str.encode('MR ' + str(distance)))
        self.ser.write(str.encode('\r\n'))
        self.counter += float(distance)
        if self.counter < 238.4 and self.counter > -29.4:
            print("position:" + str(self.counter) + "mm")
        else:
            print("Touch Bound")

    def backward(self, distance):
        self.ser.write(str.encode('MR -' + str(distance)))
        self.ser.write(str.encode('\r\n'))
        self.counter -= float(distance)
        if self.counter < 238.4 and self.counter > -29.4:
            print("position:" + str(self.counter) + "mm")
        else:
            print("Touch Bound")

    def default_speed(self):
        self.ser.write(str.encode('VM=500'))
        self.ser.write(str.encode('\r\n'))
        print("speed:500RPS")

    def set_speed(self, speed):
        self.ser.write(str.encode('VM=' + str(speed)))
        self.ser.write(str.encode('\r\n'))
        print("speed:" + str(speed) +"RPS")


