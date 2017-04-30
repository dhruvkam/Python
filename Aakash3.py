import RPi.GPIO asGPIO
import time.os 
GPIO.setmode(GPIO.BCM)
GPIO.setup (14,GPIO.OUT)
GPIO.output (14, HIGH)
time.sleep (2)
GPIO.output (14, LOW)
