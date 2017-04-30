import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
print ('ask the user to print first number')
x=int (input() )
print ('ask the user to print second number')
y=int (input () )
print (x+y)
n=(x+y)
 while n>o:
	 GPIO.output(26,HIGH)
	 time.sleep (0.5)
	 GPIO.output(26,LOW)
	 n=n-1

