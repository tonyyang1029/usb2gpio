import serial
import time

tx_data = '3D FF'
# usb2gpio = serial.Serial('/dev/tty.usbserial-10')
usb2gpio = serial.Serial(None, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
usb2gpio.setPort('/dev/tty.usbserial-10')
while True:
    usb2gpio.open()
    usb2gpio.write(bytes.fromhex(tx_data))
    usb2gpio.reset_input_buffer()
    rx_data = usb2gpio.read(103)
    rx_str = rx_data.decode()
    print(rx_data)
    usb2gpio.close()
    time.sleep(2)