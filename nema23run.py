#17 -- enable pin  || enable pin is active low
#27 -- dir +
#22 -- pul +
import RPi.GPIO as GPIO
import time
a=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
try:
    GPIO.output(17, GPIO.LOW) #enable high
    GPIO.output(27, GPIO.HIGH) #dir enable
    GPIO.output(22, GPIO.LOW) #pulse low
    while True:
        time.sleep(1)
        #val=int(input()) # uncomment this section to control the 72 degree movment || pass 1 as input 
        val=1   # comment this value if uncommenting the above one
        if val==1:
            for i in range(0,640): 
                GPIO.output(22, GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(22, GPIO.LOW)
                time.sleep(0.001)
                #time.sleep(1)
                print(a)
                a=a+1
                time.sleep(0.00001)
        else: 
            continue
        time.sleep(2)
except KeyboardInterrupt:
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW) #dir disable
        GPIO.output(17, GPIO.HIGH)
        GPIO.cleanup()
        print("exited")
