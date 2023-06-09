import serial
import time
import os

cmd_write_high = '3A 16 01'
cmd_read_high = '3D FF'
usb2gpio = serial.Serial(None, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
usb2gpio.setPort('/dev/tty.usbserial-3140')
count = 1
while True:
    print("==== No.%d ====" % count)
    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_read_high))
    rsp_cmd_read_high = usb2gpio.read(103)
    usb2gpio.write(bytes.fromhex(cmd_write_high))
    rsp_cmd_write_high = usb2gpio.read(2)
    usb2gpio.close()
    print(rsp_cmd_read_high)
    print(rsp_cmd_write_high)
    rx_str = rsp_cmd_read_high.decode()
    if rx_str.find("CH1:0") != -1:
        print("Light On")
    elif rx_str.find("CH1:1") != -1:
        print("Light Off")
    else:
        print("ERROR!!")
        break
    count += 1
    time.sleep(10)