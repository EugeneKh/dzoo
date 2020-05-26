from time import sleep
import pyautogui
import serial
ser = serial.Serial("/dev/ttyUSB2")
ser.baudrate = 9600
while True :
    line = ser.read()
    if line == b'1':
        print('ok')
    else:
        print('no')

#pyautogui.keyDown('space')
