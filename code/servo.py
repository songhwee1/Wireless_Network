import RPi.GPIO as GPIO

import time

SERVO=18

GPIO.setmode(GPIO.BCM)

GPIO.setup(SERVO,GPIO.OUT)

SERVO_PWM=GPIO.PWM(SERVO,50)

SERVO_PWM.start(0)
