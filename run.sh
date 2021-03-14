#!/usr/bin/env bash
sleep 5
python /home/pi/grow/lightController.py &
python /home/pi/grow/fanController.py &
python /home/pi/grow/humidityController.py &
python /home/pi/grow/temperatureController.py &
python /home/pi/grow/data.py &
python /home/pi/grow/data1.py &
python /home/pi/grow/data2.py &
