#17 -- enable pin 
#13 -- dir +
#19 -- dir -
#26 -- pul +
import RPi.GPIO as GPIO
import time
import os
a=0
b=370000
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
def clockwise(count):
        print("clk")
        GPIO.output(17, GPIO.LOW) #enable high
        GPIO.output(13, GPIO.HIGH) #dir enable
        GPIO.output(19, GPIO.LOW) #dir enable
        while True:
            GPIO.output(26, GPIO.HIGH)
            time.sleep(700/1000000)
            GPIO.output(26, GPIO.LOW)
            time.sleep(700/1000000)
            count=count+1
            print(count)
            if count > b:
                break

def anticlockwise(count):
        GPIO.output(17, GPIO.LOW) #enable high
        GPIO.output(13, GPIO.LOW) #dir enable
        GPIO.output(19, GPIO.HIGH) #dir enable
        while True:
            GPIO.output(26, GPIO.HIGH)
            time.sleep(700/1000000)
            GPIO.output(26, GPIO.LOW)
            time.sleep(700/1000000)
            count=count+1
            print(count)
            if count > b:
                break

print("choose clockwise /anti clockwise\n[1] : clockwise\n[2] : anticlockwise\n")
x= input(int())
GPIO.output(17, GPIO.HIGH)
GPIO.output(19, GPIO.LOW) #dir enable
GPIO.output(13, GPIO.LOW) #dir enable
GPIO.output(26, GPIO.LOW) #dir enable
if x == 1:
    count=0
    clockwise(count)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW) #dir enable
    GPIO.output(13, GPIO.LOW) #dir enable
    GPIO.output(26, GPIO.LOW) #dir enable
    GPIO.cleanup()
    print("exited")
if x == 2:
    count=0
    anticlockwise(count)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW) #dir enable
    GPIO.output(13, GPIO.LOW) #dir enable
    GPIO.output(26, GPIO.LOW) #dir enable
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
