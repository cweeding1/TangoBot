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
