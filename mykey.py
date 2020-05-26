from time import sleep
import pyautogui
import serial
ser = serial.Serial("/dev/ttyUSB2")
ser.baudrate = 9600
while True :
    data = [int(x) for x in ser.readline().split()]
    print(data)
