
import bme280
import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)

pinHumidificador = 5



GPIO.setup(pinHumidificador, GPIO.OUT)

temperature,pressure,humidity = bme280.readBME280All()

maxHum = 60
minHum = 55
hist = 3

while True:
    temperature,pressure,humidity  = bme280.readBME280All()
    if humidity != 0 : 
      if humidity <= (minHum)  :
           GPIO.output(pinHumidificador, False)
        
           print "Humidificador Encendido"
           print "Humidity : ", humidity, "%"
           time.sleep(100)


      elif humidity >= (maxHum) :
       
          GPIO.output(pinHumidificador, True)
          print "Humedad alta, humidificador apagado"
          print "Humidity : ", humidity, "%"
          time.sleep(100)

      else:
        
          GPIO.output(pinHumidificador, False)
          print "Humidificador encendido(else), ventilador apagado"
          print "Humidity : ", humidity, "%"
          time.sleep(120)
    else:
        GPIO.output(pinHumidificador, False)
        print "Humidifciador  temporizador On(error humedad igual a 0)"
        time.sleep(600)
	GPIO.output(pinHumidificador, True)
        print "Humidificador temporizador OFf(error humedad igual a 0)"
	time.sleep(180) 




