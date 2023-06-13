import serial
import time
import os
import platform


def blackscreenhunter_screenoff():
    cmd_read_lightsensor = '3D FF'
    cmd_stop_output = '3A 09 01'

    usb2gpio = serial.Serial(None, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
    if platform.system() == "Windows":
        usb2gpio.setPort('COM17')
    elif platform.system() == "Darwin":
        usb2gpio.setPort('/dev/tty.usbserial-4110')
    elif platform.system() == 'Linux':
        usb2gpio.setPort('/dev/ttyUSB0')
    else:
        return

    count = 1

    while True:
        print("==== No.%d ====" % count)
        print("Turn off screen")
        os.system("adb shell input keyevent KEYCODE_POWER")
        time.sleep(10)

        print("Turn on screen")
        os.system("adb shell input keyevent KEYCODE_POWER")
        time.sleep(10)
        usb2gpio.open()
        usb2gpio.write(bytes.fromhex(cmd_read_lightsensor))
        rsp_read_lightsensor = usb2gpio.read(103)
        usb2gpio.write(bytes.fromhex(cmd_stop_output))
        rsp_stop_output = usb2gpio.read(2)
        usb2gpio.close()
        # print(rsp_read_lightsensor)
        rsp_str = rsp_read_lightsensor.decode()
        if rsp_str.find("CH1:0") != -1:
            print("Screen On!!")
        else:
            print("ERROR!!")
            break

        time.sleep(10)
        count += 1
