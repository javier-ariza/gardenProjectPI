import RPi.GPIO as GPIO
import datetime
import time
GPIO.setmode(GPIO.BCM)
pin = 17
GPIO.setup(pin, GPIO.OUT)


while True:
        GPIO.output(pin, False)
        print "Ventilador temporizador On"
        time.sleep(300)
	GPIO.output(pin, True)
        print "Ventilador temporizador OFf"
	time.sleep(1200)
