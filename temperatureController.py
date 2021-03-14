import bme280
import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)

pinVentilador = 22

GPIO.setup(pinVentilador, GPIO.OUT)

temperature,pressure,humidity = bme280.readBME280All()

maxTemp = 26


while True:
    temperature,pressure,humidity  = bme280.readBME280All()
    if temperature != 0 :
      if temperature >= (maxTemp)  :
           GPIO.output(pinVentilador, False)
           print "Ventilador sobrecalentamiento on"
           print "Temperatura : ", temperature, "C"
           time.sleep(200)
      else:
          GPIO.output(pinVentilador, True)
          print "Ventilador apagado"
          print "Temperatura : ", temperature, "C"
          time.sleep(100)
    else: 
        GPIO.output(pinVentilador, False)
        print "Ventilador temporizador On(error temperatura igual a 0)"
        time.sleep(300)
	GPIO.output(pinVentilador, True)
        print "Ventilador temporizador OFf(error temperatura igual a 0)"
	time.sleep(1200) 

