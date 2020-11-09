#17 -- enable pin
#10 -- dir +
#9 -- dir -
#11 -- pulse +
import RPi.GPIO as GPIO
import time
import os
a=0
b=370000
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
def clockwise(count):
    try:
        print("clk")
        GPIO.output(17, GPIO.LOW) #enable high
        GPIO.output(10, GPIO.HIGH) #dir + enable
        GPIO.output(9, GPIO.LOW) #dir - disable
        while True:
            GPIO.output(11, GPIO.HIGH)
            time.sleep(700/1000000)
            GPIO.output(11, GPIO.LOW)
            time.sleep(700/1000000)
            count=count+1
            print(count)
            if count > b:
                break
    except KeyboardInterrupt:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW) #dir enable
        GPIO.cleanup()
        print("exited")

def anticlockwise(count):
    try:
        GPIO.output(17, GPIO.LOW) #enable high
        GPIO.output(10, GPIO.LOW) #dir enable
        GPIO.output(9, GPIO.HIGH) #dir enable
        while True:
            GPIO.output(11, GPIO.HIGH)
            time.sleep(700/1000000)
            GPIO.output(11, GPIO.LOW)
            time.sleep(700/1000000)
            count=count+1
            print(count)
            if count > b:
                break
    except KeyboardInterrupt:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(9, GPIO.LOW) #dir enable
        GPIO.cleanup()
        print("exited")

print("choose clockwise /anti clockwise\n[1] : clockwise\n[2] : anticlockwise\n")
x= input(int())
GPIO.output(17, GPIO.HIGH)
GPIO.output(9, GPIO.LOW) #dir enable
GPIO.output(10, GPIO.LOW) #dir enable
GPIO.output(11, GPIO.LOW) #dir enable
if x == 1:
    count=0
    clockwise(count)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW) #dir enable
    GPIO.output(11, GPIO.LOW) #dir enable
    GPIO.output(10, GPIO.LOW) #dir enable
    GPIO.cleanup()
    print("exited")
if x == 2:
    count=0
    anticlockwise(count)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW) #dir enable
    GPIO.output(11, GPIO.LOW) #dir enable
    GPIO.output(10, GPIO.LOW) #dir enable
    GPIO.cleanup()
    print("exited")
else:
    print("enter a valid value")
'''
while True:
    print("started")
    count=0
    clockwise(count)
    time.sleep(1)
    anticlockwise(count)
    time.sleep(5)
'''
