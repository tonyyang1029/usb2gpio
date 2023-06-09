import serial
import time
import os
import platform

cmd_write_high = '3A 16 01'
cmd_read_high = '3D FF'

usb2gpio = serial.Serial(None, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
if platform.system() == "Windows":
    usb2gpio.setPort('COM17')
elif platform.system() == "OS X":
    usb2gpio.setPort('/dev/tty.usbserial-3140')
else:
    exit(1)

count = 1
while True:
    print("==== No.%d ====" % count)
    print("Reboot device")
    os.system("adb reboot")
    time.sleep(40)

    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_read_high))
    rsp_cmd_read_high = usb2gpio.read(103)
    usb2gpio.write(bytes.fromhex(cmd_write_high))
    rsp_cmd_write_high = usb2gpio.read(2)
    usb2gpio.close()
    print(rsp_cmd_read_high)
    rsp_str = rsp_cmd_read_high.decode()
    if rsp_str.find("CH1:0") != -1:
        print("Light On")
    else:
        print("ERROR!!")
        break

    time.sleep(5)
    count += 1