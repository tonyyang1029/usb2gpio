import serial
import time
import platform


def luminacecontrolledpowerswitcher():
    cmd_enable_relay = '3A 09 01'
    cmd_disable_relay = '3A 09 00'
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

    print("Reset switcher")
    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_disable_relay))
    rsp_disable_relay = usb2gpio.read(2)
    usb2gpio.close()
    state = 0
    time.sleep(5)

    while True:
        usb2gpio.open()
        usb2gpio.write(bytes.fromhex(cmd_read_lightsensor))
        rsp_read_lightsensor = usb2gpio.read(103)
        usb2gpio.write(bytes.fromhex(cmd_stop_output))
        rsp_stop_output = usb2gpio.read(2)
        usb2gpio.close()
        print(rsp_read_lightsensor)
        rsp_str = rsp_read_lightsensor.decode()
        if rsp_str.find("CH1:0") != -1 and state == 0:
            print("Turn on switcher")
            usb2gpio.open()
            usb2gpio.write(bytes.fromhex(cmd_enable_relay))
            rsp_enable_relay = usb2gpio.read(2)
            usb2gpio.close()
            state = 1
        elif rsp_str.find("CH1:1") != -1 and state == 1:
            print("Turn off switcher")
            usb2gpio.open()
            usb2gpio.write(bytes.fromhex(cmd_disable_relay))
            rsp_disable_relay = usb2gpio.read(2)
            usb2gpio.close()
            state = 0
        else:
            print("Skip")

        time.sleep(10)
