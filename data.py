
import bme280
import RPi.GPIO as GPIO
import datetime
import time

temperature,pressure,humidity = bme280.readBME280All()


while True:
         temperature,pressure,humidity  = bme280.readBME280All()
         time_1 = datetime.datetime.now().strftime("%H%M")
         print  temperature, time_1
         file = open("/home/pi/grow/dataTem.txt", "a") 
         file.write(str(temperature)+ " " +  str(time_1) + '\n') 
         file.close() 
         time.sleep(120)

         



