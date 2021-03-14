
import RPi.GPIO as GPIO
import datetime
import time
GPIO.setmode(GPIO.BCM)
pin = 27
GPIO.setup(pin, GPIO.OUT)

while True:
    time_1 = datetime.datetime.now().strftime("%H:%M")
    if (time_1 >= "12:00" and time_1 <= "24:00") or (time_1>= "00:00" and time_1 <= "06:00"):
        GPIO.output(pin, False)
        print "Luz On"
        time.sleep(60)
    else:
        GPIO.output(pin, True)
        print "Luz Off"
        time.sleep(60)


