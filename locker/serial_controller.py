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
        time.sleep(2)
        self.led_off()


    def led_off(self):
        print("LED is off...")
        time.sleep(0.1)
        self.ser.write(b'L')


# def led_on_off():
#     user_input = input("\n Type on / off / quit : ")
#     if user_input =="on":
#         print("LED is on...")
#         time.sleep(0.1)
#         ser.write(b'H')
#         led_on_off()
#     elif user_input =="off":
#         print("LED is off...")
#         time.sleep(0.1)
#         ser.write(b'L')
#         led_on_off()
#     elif user_input =="quit" or user_input == "q":
#         print("Program Exiting")
#         time.sleep(0.1)
#         ser.write(b'L')
#         ser.close()
#     else:
#         print("Invalid input. Type on / off / quit.")
#         led_on_off()
#
# time.sleep(2) # wait for the serial connection to initialize
#
# led_on_off()
