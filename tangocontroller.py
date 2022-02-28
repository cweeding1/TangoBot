import serial, time, sys

class TangoController:

    def __init__(self):
        pass


def main():
    pass

try:
    usb = serial.Serial('/dev/ttyACM0')
    print(usb.name)
    print(usb.baudrate)

except:
    try:
        usb = serial.Serial('/dev/ttyACM1')
        print(usb.name)
        print(usb.baudrate)
    except:
        print("No servo serial port")
        sys.exit(0)

target = 4500 #6700

lsb = target &0x7F
msb = (target >> 7) &0x7F

cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x02) + chr(lsb) + chr(msb)

print("writing")
usb.write(cmd.encode())
print("reading")

"""
NEW CODE
"""

from tkinter import *
import serial, time, sys


class TangoController:

    def __init__(self, window):
        self.window = window

        self.waist = 6000
        self.head_vert = 6000
        self.head_horiz = 6000
        self.motor_forward = 6000
        self.motor_turn = 6000

    def forward(self, event):
        self.motor_forward += 500
        print(self.motor_forward)

    def backward(self, event):
        self.motor_forward -= 500
        print(self.motor_forward)

    def turn_right(self, event):
        self.motor_turn += 500
        print(self.motor_turn)

    def turn_left(self, event):
        self.motor_turn -= 500
        print(self.motor_turn)

    def head_up(self, event):
        self.head_vert += 500
        print(self.head_vert)

    def head_down(self, event):
        self.head_vert -= 500
        print(self.head_vert)

    def head_left(self, event):
        self.head_horiz += 500
        print(self.head_horiz)

    def head_right(self, event):
        self.head_horiz -= 500
        print(self.head_horiz)

    def waist_left(self, event):
        self.waist += 500
        print(self.waist)

    def waist_right(self, event):
        self.waist -= 500
        print(self.waist)

win = Tk()
controller = TangoController(win)

win.bind('<Up>', controller.forward)
win.bind('<Down>', controller.backward)
win.bind('<Left>', controller.turn_left)
win.bind('<Right>', controller.turn_right)

win.bind('<Key-w>', controller.head_up)
win.bind('<Key-s>', controller.head_down)
win.bind('<Key-a>', controller.head_left)
win.bind('<Key-d>', controller.head_right)

win.mainloop()

