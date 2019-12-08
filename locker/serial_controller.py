import serial
import time


class SerialController:
    def __init__(self):
        self.ser = None

    # Define the serial port and baud rate.
    def open_serial(self):
        self.ser = serial.Serial('COM1', 9600)


    def close_serial(self):
        self.ser.close()


    def led_on(self):
        print("LED is on...")
        time.sleep(0.1)
        self.ser.write(b'H')
        time.sleep(5)
        self.led_off()


    def led_off(self):
        print("LED is off...")
        time.sleep(0.1)
        self.ser.write(b'L')
