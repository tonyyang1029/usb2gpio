import serial
import time

cmd_write_high = '3A 09 01'
cmd_write_low = '3A 09 00'
usb2gpio = serial.Serial(None, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
usb2gpio.setPort('/dev/tty.usbserial-4110')
count = 1
while True:
    print("==== No.%d ====" % count)
    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_write_low))
    rsp_cmd_write_low = usb2gpio.read(2)
    print(rsp_cmd_write_low)
    time.sleep(20)
    usb2gpio.write(bytes.fromhex(cmd_write_high))
    rsp_cmd_write_high = usb2gpio.read(2)
    print(rsp_cmd_write_high)
    usb2gpio.close()

    count += 1
    time.sleep(40)