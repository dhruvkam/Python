import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM )
GPIO.setup (26,GPIO.OUT)
print("please type 1 or 2")
x= int (input ())
if x==1:
	GPIO.output (26,GPIO.HIGH)
if x==2:
	GPIO.output (26,GPIO LOW)
		
	
