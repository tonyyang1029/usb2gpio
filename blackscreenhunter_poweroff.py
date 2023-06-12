import serial
import time
import platform

cmd_enable_relay = '3A 09 01'
cmd_disable_relay = '3A 09 00'
cmd_read_lightsensor = '3D FF'
cmd_stop_output = '3A 09 01'

usb2gpio = serial.Serial(None, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
if platform.system() == "Windows":
    usb2gpio.setPort('COM17')
elif platform.system() == "Darwin":
    usb2gpio.setPort('/dev/tty.usbserial-4110')
else:
    exit(1)

count = 1

while True:
    print("==== No.%d ====" % count)

    print("Power off device")
    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_disable_relay))
    rsp_disable_relay = usb2gpio.read(2)
    usb2gpio.close()
    time.sleep(20)

    print("Power on device")
    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_enable_relay))
    rsp_enable_relay = usb2gpio.read(2)
    usb2gpio.close()
    time.sleep(30)

    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(cmd_read_lightsensor))
    rsp_read_lightsensor = usb2gpio.read(103)
    usb2gpio.write(bytes.fromhex(cmd_stop_output))
    rsp_stop_output = usb2gpio.read(2)
    usb2gpio.close()
    # print(rsp_read_lightsensor)
    rsp_str = rsp_read_lightsensor.decode()
    if rsp_str.find("CH1:0") != -1:
        print("Light On")
    else:
        print("ERROR!!")
        break

    time.sleep(10)
    count += 1